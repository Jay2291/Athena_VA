import speech_recognition as sr
from ttsaudio import speak

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