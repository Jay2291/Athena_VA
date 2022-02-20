from datetime import datetime
import wikipedia
import webbrowser as web
import os
import pywhatkit
from ttsaudio import speak
from greet import wishMe
from command import takeCommand

if __name__ == "__main__":
        wishMe()
    #while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2, auto_suggest=False)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            print("Please Wait...")
            web.open_new("youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            print("Please Wait...")
            web.open_new("google.com")

        elif 'open gmail' in query:
            speak("Opening Gmail...")
            print("Please Wait...")
            web.open_new("gmail.com")

        elif 'open stack overflow' in query:
            speak("Opening stackoverflow...")
            print("Please Wait...")
            web.open_new("stackoverflow.com")

        elif 'play' in query:
            song = query.replace("play", "")
            print("Playing "+song)
            speak("Please Wait")
            pywhatkit.playonyt(song)

        elif 'time' in query:
            strTime = datetime.datetime.now().strfttime("%H:%M:%S")
            speak(f"Right now time is {strTime}")
            print(strTime)
        
        elif 'code' in query:
            codePath = "C:\\Users\\JAY JAGTAP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Please Wait")
            print("Please Wait...")
            os.startfile(codePath)
