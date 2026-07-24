import time
import pyautogui as auto
import pyperclip
import random
import os
from google import genai
from google.genai import types
from openai import OpenAI
import webbrowser
from dotenv import load_dotenv

load_dotenv()

IS_FIRST_RUN = True

def whole_chat_bot():

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY")) #google ai studio api
    
    def last_message_from_sender(chat_log,sender_name):
        messages=chat_log.strip().split("2026]")[-1]
        if sender_name in messages:
            
            return True
        return False
    IS_FIRST_RUN = True

    def new_brain(chat_history_string):
        global IS_FIRST_RUN
        try:
            client = OpenAI(
                base_url="https://api.aicredits.in/v1",
                api_key=os.getenv("AICREDITS_API_KEY")  #aicredits api
            )
            
            # Determine how much text to send based on the run history
            if IS_FIRST_RUN:
                final_text_to_send = chat_history_string
                IS_FIRST_RUN = False  # Switch off forever after this first API call
            else:
                lines = [line.strip() for line in chat_history_string.strip().split('\n') if line.strip()]
                final_text_to_send = "\n".join(lines[-2:])
            
            formatted_messages = [
                {
                    "role": "system", 
                    "content": (
                        "You are a person named Heart Hacker who speaks bengali as well as English.Try to use banglish more than english "
                        "You are from India. You analyze chat history and talk people in a human way.Your responce should be like Heart Hacker "
                        "Output should be the next chat response (text message only). "
                        
                        "Be polite with everybody."
                        "Dont use fullstop,exclametory mark etc..in the ending"
                        "Talk normally like a human do.Don't tell extra things always try to reply their word only..sometimes extra things when needed"
                        "Give short one line response under 4,5,6 words"
                        "Do not start like this [21:02, 12/6/2024] Rohan Das:.please give short reply "
                    )
                },
                {
                    "role": "user", 
                    "content": final_text_to_send
                }
            ]
            
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=formatted_messages
            )
            
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
        
    def ai_brain(chat_history):
        try:
            response = client.models.generate_content(
                # model="gemini-3.1-flash-lite",
                model="gemini-3.5-flash-lite",
                # model="gemini-2.5-flash",
                # model="gemini-2.5-flash-lite",
                # model="gemini-3-flash",
                # model="gemini-3.5-flash",
                contents=chat_history,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        "You are a person named Heart Hacker who speaks bengali as well as Banglish.Try to use banglish more than english "
                        "You are from India. You analyze chat history and talk people in a human way.Your responce should be like Heart Hacker "
                        "Output should be the next chat response (text message only). "
                        "You are talking to my sister,say tumi not tui"
                        "Be polite with everybody."
                        "Dont use fullstop,exclametory mark etc..in the ending"
                        "Talk normally like a human do.Don't tell extra things always try to reply their word only..sometimes extra things when needed"
                        "Give short one line response under 4,5,6 words"
                        "Do not start like this [21:02, 12/6/2024] Rohan Das:.please give short reply "
                        "First letter of the sentense should be capital, and talk fully human like"
                    )
                )
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"
    
    webbrowser.open("https://web.whatsapp.com/")
    time.sleep(random.randint(10,20))
    
    auto.click(371,445)
    time.sleep(1.5)
    auto.click(1155,149)
    time.sleep(1.5)
    auto.click(1881,143)
    time.sleep(0.5)
    auto.hotkey("ctrl","a")
    time.sleep(0.5)
    auto.hotkey("ctrl","c")
    info_name=pyperclip.paste()
    auto.click(1381,146)
    time.sleep(1)
    auto.click(1381,146)
    time.sleep(1)

    while True:
        auto.moveTo(696,206)
        time.sleep(3)
        auto.dragTo(1864,931,duration=3, button='left')
        time.sleep(0.5)
        auto.hotkey("ctrl","c")
        time.sleep(0.5)
        auto.click(1084,436)
        time.sleep(0.5)
        chat=pyperclip.paste()
        time.sleep(2)
        if last_message_from_sender(chat,info_name):
            

            output=ai_brain(chat)
            # output=new_brain(chat)
            if output.lower().startswith("error"):
                print(output)
                output=random.choice(["Pore kotha bolchi",
                                    "Ektu pore aschi",
                                    "Ghumiye ja ami aschi ektu por",
                                    "Kaj korchi dara aschi"
                                    ])
            pyperclip.copy(output)
            auto.click(1331,972)

            auto.hotkey("ctrl","v")
            time.sleep(2)
            auto.press('enter')
            

def youtube(gan):
    webbrowser.open("www.youtube.com")
    time.sleep(5.5)
    auto.click(680,144)
    time.sleep(0.5)
    auto.write(gan)
    time.sleep(0.5)
    auto.press('enter')
    time.sleep(3)
    auto.moveTo(738,797)
    time.sleep(1)
    auto.click(738,797)