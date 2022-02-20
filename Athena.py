import wikipedia
import webbrowser as web
import os
import pywhatkit
from ttsaudio import speak
from greeting import wishMe
from command import takeCommand

if __name__ == "__main__":
    #wishMe()
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