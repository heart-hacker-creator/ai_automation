# 🤖 Jarvis AI Assistant & WhatsApp Automation Bot

A feature-rich **Voice-Controlled AI Assistant (Jarvis)** and **Automated WhatsApp Chatbot (Heart Hacker)** built with Python, Google Gemini AI, Speech Recognition, GUI Automation, and a **Futuristic Sci-Fi Web HUD Interface**.

---

## ✨ Features

### 🌐 1. Futuristic Sci-Fi Web Interface (`app.py`, `index.html`)
- **Glowing Arc Reactor Visualizer**: Interactive central mic button with animated spinning rings and soundwave visualizers.
- **Browser Voice Recognition**: Tap the Arc Reactor to speak directly into your browser using Web Speech API.
- **Live Command Console**: Real-time message feed displaying user prompts and Jarvis's AI replies.
- **Quick Action Pills**: Fast triggers for Weather reports, News headlines, YouTube music playback, and WhatsApp Bot.

---

### 🎙️ 2. Jarvis Voice Engine (`1_main.py`)
- **Wake Word Activation**: Listens for the wake word `"Jarvis"` via microphone.
- **Google Gemini AI Integration**: Powered by Google's latest Gemini models for human-like conversational intelligence.
- **Voice Response System**: Converts text to speech using `pyttsx3` and `gTTS`.
- **Web Navigation**: Voice commands to open YouTube, Facebook, Instagram, LinkedIn, and WhatsApp Web.
- **🌤️ Live Weather Updates**: Real-time temperature and weather conditions via WeatherAPI.
- **📰 Top News Headlines**: Reads out the top news headlines via NewsAPI.
- **🎵 Music Playback**: Plays requested songs directly on YouTube or from a predefined dictionary.

---

### 💬 3. WhatsApp Auto Chatbot (`chat_bot_code.py`)
- **GUI Automation**: Uses `pyautogui` and `pyperclip` to interact with WhatsApp Web.
- **Smart Contact Detection**: Dynamically captures contact details and chat history.
- **AI Persona ("Heart Hacker")**: Responds in natural, friendly Banglish/English with short, human-like chat replies.

---

## 📁 Repository Structure

```
├── app.py             # Flask Web Server connecting Web HUD to Jarvis backend
├── index.html         # Futuristic Sci-Fi HUD Dashboard HTML
├── style.css          # Sci-Fi dark theme & Arc Reactor animations
├── script.js          # Web Speech API & frontend interactivity
├── 1_main.py          # Core voice assistant logic & Gemini AI brain
├── chat_bot_code.py   # WhatsApp automation & AI chatbot engine
├── functions.py       # WeatherAPI utility & helper functions
├── music.py           # Quick-play song dictionary mapping
├── main.py            # Screen coordinate utility script
├── texts.py           # Local app launcher snippets
├── .env.example       # Template for API keys
├── .gitignore         # Prevents committing secrets & temp files
└── requirements.txt   # Required Python packages
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/heart-hacker-creator/ai_automation.git
cd ai_automation
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Copy `.env.example` to `.env` and fill in your keys:
```env
GEMINI_API_KEY=your_gemini_api_key_here
NEWS_API_KEY=your_news_api_key_here
WEATHER_API_KEY=your_weather_api_key_here
AICREDITS_API_KEY=your_aicredits_api_key_here
```

---

## 🎮 How to Run

### 🌐 Method A: Launch Sci-Fi Web HUD (Recommended)
```bash
python app.py
```
This automatically starts your local Flask server on `http://127.0.0.1:5000` and opens the futuristic visual interface in your browser!

### 🎙️ Method B: Run Terminal Voice Assistant
```bash
python 1_main.py
```

---

## 🛡️ Privacy & Security
Personal API keys and runtime files are kept secure using `.env` and `.gitignore` to prevent sensitive credentials from being leaked.

---

## 👨‍💻 Created By
Developed by **Heart Hacker** 🚀
