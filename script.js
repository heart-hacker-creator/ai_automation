// ==========================================================================
// JARVIS HUD DASHBOARD SCRIPT (Speech Recognition & API Integration)
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const micBtn = document.getElementById('micBtn');
    const reactorStateText = document.getElementById('reactorStateText');
    const subStateText = document.getElementById('subStateText');
    const soundWave = document.getElementById('soundWave');
    const voiceStatusPill = document.getElementById('voiceStatusPill');
    const commandInput = document.getElementById('commandInput');
    const sendBtn = document.getElementById('sendBtn');
    const chatBox = document.getElementById('chatBox');
    const clearChatBtn = document.getElementById('clearChatBtn');
    const clockDisplay = document.getElementById('clockDisplay');
    const actionChips = document.querySelectorAll('.action-chip');

    let isListening = false;
    let recognition = null;

    // 1. Clock Display
    function updateClock() {
        const now = new Date();
        clockDisplay.textContent = now.toLocaleTimeString();
    }
    setInterval(updateClock, 1000);
    updateClock();

    // 2. Initialize Web Speech Recognition
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (SpeechRecognition) {
        recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        recognition.onstart = () => {
            isListening = true;
            micBtn.classList.add('listening');
            soundWave.classList.add('active');
            reactorStateText.textContent = "LISTENING...";
            subStateText.textContent = "Speak your command clearly into your microphone";
            voiceStatusPill.innerHTML = `<i class="fa-solid fa-microphone-lines"></i> RECORDING`;
            voiceStatusPill.style.borderColor = '#ff0055';
            voiceStatusPill.style.color = '#ff0055';
        };

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            console.log("Recognized speech:", transcript);
            commandInput.value = transcript;
            submitCommand(transcript);
        };

        recognition.onerror = (event) => {
            console.error("Speech Recognition Error:", event.error);
            stopListening();
            reactorStateText.textContent = "SPEECH ERROR";
            subStateText.textContent = `Error: ${event.error}. Click mic to try again.`;
        };

        recognition.onend = () => {
            stopListening();
        };
    } else {
        subStateText.textContent = "Web Speech API not supported in this browser. Use text input below.";
        voiceStatusPill.textContent = "NO MIC API";
    }

    function stopListening() {
        isListening = false;
        micBtn.classList.remove('listening');
        soundWave.classList.remove('active');
        reactorStateText.textContent = "TAP TO SPEAK TO JARVIS";
        subStateText.textContent = "Listening to wake word or voice commands";
        voiceStatusPill.innerHTML = `<i class="fa-solid fa-microphone"></i> READY`;
        voiceStatusPill.style.borderColor = 'rgba(0, 243, 255, 0.25)';
        voiceStatusPill.style.color = '#e0f7fc';
    }

    // Mic Toggle Event
    micBtn.addEventListener('click', () => {
        if (!recognition) return;
        if (isListening) {
            recognition.stop();
        } else {
            recognition.start();
        }
    });

    // 3. Command Submission Handler
    async function submitCommand(commandText) {
        if (!commandText || commandText.trim() === '') return;

        const command = commandText.trim();
        commandInput.value = '';

        // Add User Message to Chat Log
        appendMessage('USER', command, 'user-msg');

        // Show Processing state
        reactorStateText.textContent = "PROCESSING...";
        subStateText.textContent = "Jarvis is analyzing your request...";
        soundWave.classList.add('active');

        try {
            const response = await fetch('/api/command', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ command: command })
            });

            const data = await response.json();

            if (data.status === 'success') {
                appendMessage('JARVIS AI', data.response, 'system-msg');
                speakTextInBrowser(data.response);
            } else {
                appendMessage('JARVIS AI', `Error: ${data.message || 'Failed to process command'}`, 'system-msg');
            }
        } catch (err) {
            console.error("API Fetch Error:", err);
            appendMessage('JARVIS AI', "Connection error: Unable to reach Jarvis backend server.", 'system-msg');
        } finally {
            stopListening();
        }
    }

    // Browser Speech Synthesis (Web Voice Feedback)
    function speakTextInBrowser(text) {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel(); // Stop any active speech
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.rate = 1.0;
            utterance.pitch = 1.0;
            window.speechSynthesis.speak(utterance);
        }
    }

    // Append Message to Chat Log UI
    function appendMessage(sender, text, typeClass) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${typeClass}`;
        
        const avatarIcon = typeClass === 'user-msg' ? 'fa-user' : 'fa-robot';
        const now = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

        msgDiv.innerHTML = `
            <div class="avatar"><i class="fa-solid ${avatarIcon}"></i></div>
            <div class="msg-content">
                <span class="sender">${sender}</span>
                <p>${escapeHtml(text)}</p>
                <span class="time-stamp">${now}</span>
            </div>
        `;

        chatBox.appendChild(msgDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function escapeHtml(str) {
        return str.replace(/[&<>"']/g, function(m) {
            return {
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                '"': '&quot;',
                "'": '&#039;'
            }[m];
        });
    }

    // Input Event Listeners
    sendBtn.addEventListener('click', () => {
        submitCommand(commandInput.value);
    });

    commandInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            submitCommand(commandInput.value);
        }
    });

    // Quick Action Chips Listener
    actionChips.forEach(chip => {
        chip.addEventListener('click', () => {
            const cmd = chip.getAttribute('data-command');
            if (cmd) {
                submitCommand(cmd);
            }
        });
    });

    // Clear Chat Log
    clearChatBtn.addEventListener('click', () => {
        chatBox.innerHTML = `
            <div class="message system-msg">
                <div class="avatar"><i class="fa-solid fa-robot"></i></div>
                <div class="msg-content">
                    <span class="sender">JARVIS AI SYSTEM</span>
                    <p>Console cleared. Standing by for new commands, Boss.</p>
                    <span class="time-stamp">Just now</span>
                </div>
            </div>
        `;
    });
});
