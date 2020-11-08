import speech_recognition as sr
import pyttsx3
import requests
import json
from actions import maryHour, maryToday, maryRemind, maryCheckReminder, maryWiki, maryWeather

speaker = pyttsx3.init()
#rate = speaker.getProperty("rate")
speaker.setProperty("rate", 150)
#voices = speaker.getProperty("voices")
#speaker.setProperty("voice", "female2")
r = sr.Recognizer()

def main():
    with sr.Microphone() as source:
        while True:
            tmp = open("tmp.txt", "r")
            reminder = tmp.read()
            if reminder:
                text = maryCheckReminder(reminder)
                if text:
                    speaker.say(text)
                    speaker.runAndWait()

            print("I'm listening")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                text = text.lower()
                print("You said: " + text)
                if "mary" in text:
                    if "time" in text:
                        time = maryHour()
                        speaker.say("It is " + time)
                        speaker.runAndWait()

                    if "weather" in text:
                        weather = maryWeather()
                        speaker.say("The current weather is " + weather)
                        speaker.runAndWait()
                    
                    if "today" in text:
                        today = maryToday()
                        speaker.say("Today is " + today)
                        speaker.runAndWait()

                    if "play" in text:
                        pass

                    if "reminder" in text:
                        textNumber = [int(char) for char in text.split() if char.isdigit()]
                        number = textNumber[0]
                        if "minute" in text:
                            reminderEndTime = maryRemind(number, "minutes")
                            tmp = open("tmp.txt", "w")
                            tmp.write(reminderEndTime)
                            tmp.close()
                        
                        elif "hour" in text:
                            reminderEndTime = maryRemind(number, "hours")
                            tmp = open("tmp.txt", "w")
                            tmp.write(reminderEndTime)
                            tmp.close()

                        else:
                            speaker.say("Sorry I could not set a reminder, try again")

                    if "google" in text:
                        query = text.split("google ")
                        search = query[1]
                        summary = maryWiki(search)
                        speaker.say(summary)
                        speaker.runAndWait()
            except:
                print("Sorry, I did not recognize your voice")

if __name__ == "__main__":
    main()