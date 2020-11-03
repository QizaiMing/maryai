import requests
from datetime import datetime

def maryHour():
    now = datetime.now()
    currentTime = now.strftime("%I:%M %p")
    return currentTime

def maryToday():
    now = datetime.now()
    today = now.strftime("%A, %B %d, %Y")
    return today

def maryRemind(number=3, magnitude="minutes"):
    # currentTime = maryHour()
    # if currentTime == endTime:
    #     print("BEEP BOOP")
    print(number, magnitude)