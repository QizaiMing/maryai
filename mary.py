import speech_recognition as sr
import pyttsx3
import requests
import json
from actions import maryHour

speaker = pyttsx3.init()
#rate = speaker.getProperty("rate")
speaker.setProperty("rate", 150)
#voices = speaker.getProperty("voices")
speaker.setProperty("voice", "female2")
r = sr.Recognizer()

def maryListen(source):
    print("I'm listening")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        if "Mary" in text:
            if "time" in text:
                speaker.say("it is " + maryHour())

            elif "weather" in text:
                pass
            
            elif "today" in text:
                pass

            elif "play" in text:
                pass

            elif "reminder" in text:
                pass

            elif "goole" in text:
                pass

            else:
                speaker.say("Hey!")
            speaker.runAndWait()

    except:
        print("Sorry, I did not recognize your voice")

with sr.Microphone() as source:
    while True:
        maryListen(source)