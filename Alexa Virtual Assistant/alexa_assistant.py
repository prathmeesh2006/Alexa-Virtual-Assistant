import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import asyncio
import requests
from deep_translator import GoogleTranslator

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

API_KEY = "e208d337a306a98cbbc6e6c952c69bed"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(f"User Command: {command}")
                return command
    except Exception as e:
        print(f"Error: {e}")
        return ""
    return ""

async def translate_text(text, dest_lang):
      return GoogleTranslator(source='auto', target=dest_lang).translate(text)

def get_weather(city):
    try:
        url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            weather_report = f"The temperature in {city} is {temperature}°C with {description}."
            return weather_report
        else:
            return "Sorry, I couldn't find the weather for that city."
    except Exception as e:
        print(f"Weather API Error: {e}")
        return "Sorry, I couldn't fetch the weather."

def run_alexa():
    command = take_command()
    
    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {time}')
    
    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        info = wikipedia.summary(person, sentences=1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('Sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with Wi-Fi')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'translate' in command:
        try:
            text_to_translate = command.replace('translate', '').strip()
            translated_text = asyncio.run(translate_text(text_to_translate, 'es'))
            talk(f"The translation in Spanish is {translated_text}")
        except Exception as e:
            print(f"Translation Error: {e}")
            talk("Sorry, I couldn't translate that.")

    elif 'weather' in command:
        city = command.replace('weather', '').strip()
        if city:
            weather_report = get_weather(city)
            print(weather_report)
            talk(weather_report)
        else:
            talk("Please specify a city.")

    else:
        talk("Please say the command again.")

while True:
    run_alexa()