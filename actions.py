import requests
from datetime import datetime, timedelta
import wikipedia

def maryHour():
    now = datetime.now()
    currentTime = now.strftime("%I:%M %p")
    return currentTime #string

def maryToday():
    now = datetime.now()
    today = now.strftime("%A, %B %d, %Y")
    return today #string

def maryRemind(number, magnitude):
    if magnitude == "minutes":
        endTime = datetime.now() + timedelta(minutes=number)
    else:
        endTime = datetime.now() + timedelta(hours=number)

    formatedEndTime = endTime.strftime("%I:%M %p")
    return formatedEndTime #string

def maryCheckReminder(endTime):
    currentTime = maryHour()
    if currentTime == endTime:
        text = "BEEP BOOP, reminder, BEEP BOOP reminder, BEEP BOOP reminder, BEEP BOOP reminder, BEEP BOOP reminder"
        tmp = open("tmp.txt", "w")
        tmp.write("")
        tmp.close()
        return text

def maryWiki(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except:
        return "Sorry I did not find that result"