import speech_recognition as sr
import requests
import pyttsx3

SERVER = "https://your-codespace-url/send"
TOKEN = "ULTRA_JARVIS_123"

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):

    print("Jarvis:", text)

    engine.say(text)
    engine.runAndWait()

speak("Jarvis online")

while True:

    with sr.Microphone() as source:

        print("Listening...")

        audio = r.listen(source)

    try:

        text = r.recognize_google(audio).lower()

        print("You:", text)

        if "hey jarvis open chrome" in text:

            speak("Opening chrome")

            requests.get(
                SERVER,
                params={
                    "token": TOKEN,
                    "cmd": "start chrome"
                }
            )

    except:
        pass
