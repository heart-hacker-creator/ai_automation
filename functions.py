import requests
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": city
    }

    response = requests.get(url, params=params)
    data = response.json()

    weather = (
        f"The current weather in {data['location']['name']}, "
        f"{data['location']['country']} is {data['current']['condition']['text']}. "
        f"The temperature is {data['current']['temp_c']} degrees Celsius, "
        f"feels like {data['current']['feelslike_c']} degrees. "
        f"Humidity is {data['current']['humidity']} percent, "
        f"and the wind speed is {data['current']['wind_kph']} kilometers per hour."
    )

    return weather
def local_opening():
    pass