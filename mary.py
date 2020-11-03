import speech_recognition as sr
import pyttsx3
import requests
import json
from actions import maryHour, maryToday, maryRemind

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
                speaker.say("It is " + maryHour())

            if "weather" in text:
                pass
            
            if "today" in text:
                today = maryToday()
                speaker.say("Today is " + today) 

            if "play" in text:
                pass

            if "reminder" in text:
                textNumber = [int(char) for char in text.split() if char.isdigit()]
                if "minute" in text:
                    print("calling maryremind")
                    maryRemind(textNumber, "minutes")
                
                elif "hour" in text:
                    maryRemind(textNumber, "hours")

                else:
                    speaker.say("Sorry I could not set a reminder, try again")

            if "google" in text:
                pass

            # else:
            #     speaker.say("Hey!")
            speaker.runAndWait()

    except:
        print("Sorry, I did not recognize your voice")

with sr.Microphone() as source:
    while True:
        maryListen(source)