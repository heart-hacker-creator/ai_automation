# 🤖 Jarvis AI Assistant & WhatsApp Automation Bot

A feature-rich **Voice-Controlled AI Assistant (Jarvis)** and **Automated WhatsApp Chatbot (Heart Hacker)** built with Python, Google Gemini AI, Speech Recognition, and GUI Automation.

---

## ✨ Features

### 🎙️ 1. Jarvis Voice Assistant (`1_main.py`)
- **Wake Word Recognition**: Listens for the wake word `"Jarvis"` to activate.
- **Google Gemini AI Integration**: Powered by Google's latest Gemini models for human-like conversational responses.
- **Voice Response System**: Converts text to speech using `pyttsx3` and `gTTS`.
- **Web Navigation**: Instant voice commands to open YouTube, Facebook, Instagram, LinkedIn, and WhatsApp Web.
- **🌤️ Live Weather Updates**: Fetches real-time temperature, condition, humidity, and wind speed for any city using WeatherAPI.
- **📰 Top News Headlines**: Reads out the top news headlines via NewsAPI.
- **🎵 Music Playback**: Plays requested songs directly on YouTube or from a predefined dictionary.

---

### 💬 2. WhatsApp Auto Chatbot (`chat_bot_code.py`)
- **GUI Automation**: Uses `pyautogui` and `pyperclip` to interact with WhatsApp Web.
- **Smart Contact Detection**: Dynamically captures contact details and chat history.
- **AI Persona ("Heart Hacker")**: Responds in natural, friendly Banglish/English with short, human-like chat replies.
- **Fallback Protection**: Smart auto-reply fallbacks if an API limit or network error occurs.

---

## 📁 Repository Structure

```
├── 1_main.py          # Main voice assistant script (Jarvis)
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
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and add your API keys:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   NEWS_API_KEY=your_news_api_key_here
   WEATHER_API_KEY=your_weather_api_key_here
   AICREDITS_API_KEY=your_aicredits_api_key_here
   ```

---

## 🎮 How to Run

### Run Voice Assistant (Jarvis)
```bash
python 1_main.py
```
* **Say "Jarvis"** to wake the assistant.
* Try voice commands like:
  - `"Open YouTube"`
  - `"What is the weather in Kolkata?"`
  - `"Tell me the news"`
  - `"Play Skyfall"`
  - `"Run WhatsApp"` (launches the WhatsApp chatbot)

### Run WhatsApp Bot Standalone
```bash
python chat_bot_code.py
```

---

## 🛡️ Privacy & Security
Personal API keys and runtime files are kept secure using `.env` and `.gitignore` to prevent any sensitive credentials from being shared publicly.

---

## 👨‍💻 Created By
Developed by **Heart Hacker** 🚀
