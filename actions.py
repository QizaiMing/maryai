import requests
from datetime import datetime, timedelta
import wikipedia
import json
JOKEURL = "https://official-joke-api.appspot.com/jokes/general/random"
URL = "https://www.metaweather.com/api/location/"
CITY = "caracas"

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

def maryWeather(query=CITY):
    woeidUrl = "search/?query={}".format(query)
    endPoint = URL + woeidUrl

    try:
        response = requests.get(endPoint)
        data = response.json()
        woeid = data[0]["woeid"]
        weatherResponse = requests.get(URL + str(woeid))

        weatherJson = weatherResponse.json()
        weather = weatherJson["consolidated_weather"][0]["weather_state_name"]
        temperature = int(weatherJson["consolidated_weather"][0]["the_temp"])
        text = "the current weather is {0}, with a temperature of {1} degrees".format(weather, temperature)
        return text

    except:
        return "sorry an error occurred while I was looking for the weather"

def maryJoke():
    try:
        response = requests.get(JOKEURL)
        jokeResponse = response.json()
        setup = jokeResponse[0]["setup"]
        punchline = jokeResponse[0]["punchline"]
        joke = {
            "setup": setup,
            "punchline": punchline
        }
        err = False
        return joke, err  #dict, boolean
    
    except:
        err = True
        info = "sorry an error occurrend while I was looking for a joke"
        return info, err