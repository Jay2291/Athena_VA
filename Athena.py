from email.mime import audio
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as web
import os
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Allow me to introduce myself, I am Athena, a virtual Artificial Intelligence, and I am here to assist you with a variety of tasks as best I can. How may I help you today, Sir?")

#converts Speech through microphone to text
def takeCommand():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("I'm not sure I understand what you mean. Could you say that again...")
        speak("I'm not sure I understand what you mean. Could you say that again...")
        return "None"
    return query


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