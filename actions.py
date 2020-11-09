import requests
from datetime import datetime, timedelta
import wikipedia
import json
JOKEURL = "https://official-joke-api.appspot.com/jokes/general/random"
URL = "https://www.metaweather.com/api/location/"

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

def maryWeather(query="caracas"):
    woeidUrl = "search/?query={}".format(query)
    endPoint = URL + woeidUrl

    response = requests.get(endPoint)
    data = response.json()
    woeid = data[0]["woeid"]
    weatherResponse = requests.get(URL + str(woeid))

    weatherJson = weatherResponse.json()
    weather = weatherJson["consolidated_weather"][0]["weather_state_name"]
    temperature = int(weatherJson["consolidated_weather"][0]["the_temp"])
    text = "{0}, with {1} degrees".format(weather, temperature)
    return text

def maryJoke():
    response = requests.get(JOKEURL)
    joke = response.json()
    setup = joke[0]["setup"]
    punchline = joke[0]["punchline"]
    return setup, punchline