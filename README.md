# MaryAI
A personal assistant like Alexa or Siri based on Python<br />
<strong>Requirements</strong><br />
- A working microphone plugged in<br />

<strong>Installation (inside virtualvenv recommended)</strong><br />
```
pip install -r requirements.txt
python mary.py
```
<strong>Additional Config</strong>
```
#actions.py
CITY=your_city_of_choice
```

<strong>Available Commands</strong><br />
In order to execute a command you should say "Mary" when you ask for something, it doesn't matter the order, you just have to call her by her name.
- Tell the time: KEYWORD = "time". Example: "Hey Mary, what time is it?".
- Tell the weather: KEYWORD = "weather". Example: "Hey Mary, how is the weather?" (default city is "caracas" but you can edit it as shown above).
- What day is today: KEYWORD = "today". Example: "Hey Mary, what day is today?".
- Tell a joke: KEYWORD = "joke". Example: "Hey Mary, tell me a joke".
- Set a reminder: KEYWORDS = "reminder", "(a number)", "(minutes or hours)". Example: "Hey Mary, set a reminder in 45 minutes".
- Google a definition: KEYWORDS = "google", "(word you want to google)". Example: "Hey Mary, google democracy" (the order matters in this one since Mary will take the word righ after "google" and search for it. Sentences like "Hey Mary, google ABOUT democracy" won't work).
<br />
<strong>Tools:</strong><br />
- Pyttsx3 Python Package<br />
- Speech Recognition Python Package<br />
- Pyaudio Python Package<br />
- Wikipedia Python Package
