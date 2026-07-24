import os
import sys
import webbrowser
import threading
from flask import Flask, render_template, request, jsonify, send_from_directory
try:
    from flask_cors import CORS
    HAS_CORS = True
except ImportError:
    HAS_CORS = False

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import core Jarvis logic modules
import importlib
main_module = importlib.import_module("1_main")
import functions
import music
import chat_bot_code

app = Flask(__name__, static_folder='.', template_folder='.')
if HAS_CORS:
    CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "ONLINE",
        "system": "JARVIS HUD v2.0",
        "model": "Gemini 3.6 Flash",
        "active": True
    })

@app.route('/api/command', methods=['POST'])
def handle_command():
    data = request.json or {}
    user_command = data.get('command', '').strip()
    
    if not user_command:
        return jsonify({"error": "No command provided"}), 400

    response_text = ""
    action_taken = "text_reply"

    try:
        cmd_lower = user_command.lower()

        if "open youtube" in cmd_lower:
            webbrowser.open("https://www.youtube.com/")
            response_text = "Opening YouTube for you, Boss."
            action_taken = "web_navigation"
        elif "open facebook" in cmd_lower:
            webbrowser.open("https://www.facebook.com/")
            response_text = "Opening Facebook."
            action_taken = "web_navigation"
        elif "open instagram" in cmd_lower:
            webbrowser.open("https://www.instagram.com/")
            response_text = "Opening Instagram."
            action_taken = "web_navigation"
        elif "open linkedin" in cmd_lower:
            webbrowser.open("https://in.linkedin.com/")
            response_text = "Opening LinkedIn."
            action_taken = "web_navigation"
        elif "open whatsapp" in cmd_lower:
            webbrowser.open("https://web.whatsapp.com/")
            response_text = "Opening WhatsApp Web."
            action_taken = "web_navigation"
        elif "weather" in cmd_lower:
            place = cmd_lower.split()[-1]
            weather_output = functions.get_weather(place)
            response_text = weather_output
            action_taken = "weather"
        elif cmd_lower.startswith("launch"):
            functions.local_opening(cmd_lower)
            response_text = f"Launching requested local application."
            action_taken = "app_launch"
        elif cmd_lower.startswith("play"):
            song = cmd_lower.replace("play ", "").strip()
            if song in music.MusicDict:
                link = music.MusicDict[song]
                webbrowser.open(link)
                response_text = f"Playing {song} on YouTube."
            else:
                threading.Thread(target=chat_bot_code.youtube, args=(song,)).start()
                response_text = f"Searching and playing {song} on YouTube."
            action_taken = "music"
        elif "news" in cmd_lower:
            news_api = os.getenv("NEWS_API_KEY")
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}"
            import requests
            res = requests.get(url)
            news_data = res.json()
            articles = news_data.get("articles", [])
            titles = [art["title"] for art in articles[:3]]
            response_text = "Here are the top headlines:\n" + "\n• ".join(titles)
            action_taken = "news"
        elif "run whatsapp bot" in cmd_lower or "run whatsapp" in cmd_lower:
            threading.Thread(target=chat_bot_code.whole_chat_bot).start()
            response_text = "Running automated WhatsApp chatbot in background."
            action_taken = "bot_launch"
        else:
            response_text = main_module.ai_brain(user_command)
            action_taken = "ai_brain"

        # Speak response in background thread so server stays fast
        threading.Thread(target=main_module.speak, args=(response_text,)).start()

        return jsonify({
            "status": "success",
            "command": user_command,
            "response": response_text,
            "action": action_taken
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    print("🚀 Starting Jarvis Web HUD Server on http://127.0.0.1:5000")
    webbrowser.open("http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)
