import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import requests
from google import genai
import os
from gtts import gTTS
from playsound import playsound
import chat_bot_code
from google.genai import types
from dotenv import load_dotenv
import functions

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
news_api = os.getenv("NEWS_API_KEY")

# IS_FIRST_RUN = True
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def speak_advance(text): #I can chane it from speak_advance() to speak() to use it

    try:
        # 1. Convert the text to speech using Google's engine
        tts = gTTS(text=text, lang="en", tld="com")
        
        # 2. Save it as a temporary MP3 file
        filename = "temp_voice.mp3"
        tts.save(filename)
        
        # 3. Play the audio file
        playsound(filename)

        # 4. Delete the file so it's clean for the next command
        os.remove(filename)
        
    except Exception as e:
        print(f"Speech Error: {e}")

def ai_brain(user_prompt):
        try:                            
            response = client.models.generate_content(
                # model="gemini-3.1-flash-lite",
                model="gemini-3.6-flash",
                # model="gemini-2.5-flash",
                # model="gemini-2.5-flash-lite",
                # model="gemini-3-flash",
                # model="gemini-3.5-flash",
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        "You have to give short responses"
                        "Give me to the point answers"
                        "Don't tell extra things only to the point answers"
                        "Talk like human"
                    )
                )
            )
            return response.text 
        except Exception as e:
            return f"Error: {e}"

def ProcessCommand(c):
    if "open youtube" in c.lower():
        print(f"You said: {c}")
        webbrowser.open("https://www.youtube.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://in.linkedin.com/")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
        chat_bot_code.time.sleep(5)
        chat_bot_code.auto.click(1236,1053)
    elif "weather" in c.lower():
        place=c.lower().split()[-1]
        weather_output=functions.get_weather(place)
        print(weather_output)
        speak(weather_output)
    elif c.lower().startswith("launch"):
        functions.local_opening(c)
    elif c.lower().startswith("open"):
        c = c.replace("open ", "")
        command=f"Give me link of this page {c},Give nothing only the link"
        link=str(ai_brain(command))
        webbrowser.open(link)
    elif c.lower().startswith("play"):
        song=c.lower().replace("play ","")
        if song in music.MusicDict:
            link=music.MusicDict[song]
            webbrowser.open(link)
        else:
            chat_bot_code.youtube(song)
    elif "news" in c.lower():
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}"
        try:
            response = requests.get(url)
            data = response.json()
            articles = data.get("articles", [])
            for article in articles[:3]:
                title = article["title"]
                print(title)
                speak(title)
        except Exception as e:
            print(f"Error: {e}")
    else:
        reply=ai_brain(c)
        print(f"Jarvis:{reply}")
        speak(reply)
    print(f"You said: {c}")

if __name__ == "__main__":
    speak("Initializing Jarvis. Jarvis is now starting....")
    
    
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5)
            
            print("Recognizing...")
            word = r.recognize_google(audio)
            print(f"You said: {word}")
            if "exit" in word or "stop" in word:
                        speak("Goodbye, Boss.")
                        break  
            
            if word.lower()=="jarvis":
                speak("Yes Boss")
                print("Yes Boss")
                while True:
                    with sr.Microphone() as source:
                        print("Jarvis is active...")
                        audio=r.listen(source)
                        command=r.recognize_google(audio)
                        if "exit" in command.lower() or "stop" in command.lower():
                            speak("Goodbye, Boss.")
                            break  
                        if "run whatsapp" in command.lower():
                            speak("Ok Boss, I am running chatbot for your whatsapp")
                            chat_bot_code.whole_chat_bot()
                        ProcessCommand(command)
                    

                 
        except Exception as e:
            print("Error: {0}".format(e))
