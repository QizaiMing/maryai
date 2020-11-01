import requests
from datetime import datetime

def maryHour():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    return current_time