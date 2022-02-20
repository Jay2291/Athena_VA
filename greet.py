import datetime
from ttsaudio import speak

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Allow me to introduce myself, I am Athena, a virtual Artificial Intelligence, and I am here to assist you with a variety of tasks as best I can. How may I help you today, Sir?")
