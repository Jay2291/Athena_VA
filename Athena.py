import datetime
import time
import sys
import wikipedia
import webbrowser as web
import os
import pywhatkit
import pyjokes
from ttsaudio import speak
from greet import wishMe
from command import takeCommand

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        time.sleep(4)
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2, auto_suggest=False)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'about' in query:
            speak('Searching Wikipedia')
            query = query.replace("about", "")
            results = wikipedia.summary(query, sentences=2, auto_suggest=False)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'who is' in query:
            speak('Searching Wikipedia')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2, auto_suggest=False)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'what' in query:
            speak('Searching Wikipedia')
            query = query.replace("what", "")
            results = wikipedia.summary(query, sentences=2, auto_suggest=False)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'search' in query:
            query = query.replace("search", "")
            sear = 'https://www.google.com/search?q='+query
            print("Please wait...")
            speak("searching")
            web.open(sear)

        elif 'are you' in query:
            print("Allow me to introduce myself, I am Athena, a virtual Artificial Intelligence, and I am here to assist you with a variety of tasks as best I can.")
            speak("Allow me to introduce myself, I am Athena, a virtual Artificial Intelligence, and I am here to assist you with a variety of tasks as best I can.")

        elif 'open youtube' in query:
            print("Please Wait...")
            speak("Opening YouTube...")
            web.open_new("youtube.com")

        elif 'do' in query:
            print('''I can play songs on youtube, \ntell you a joke, search on wikipedia, \ntell date and time, \nfind your location, \nlocate areas on map, \nopen different websites like instagram, youtube, gmail, github, twitter, stackoverflow, and searches on google. So how may I help you Sir?''')
            speak('''I can play songs on youtube, \ntell you a joke, search on wikipedia, \ntell date and time, \nfind your location, \nlocate areas on map, \nopen different websites like instagram, youtube, gmail, gitHub, twitter, stackoverflow, and searches on google. \nSo how may I help you Sir?''')

        elif 'open google' in query:
            print("Please Wait...")
            speak("Opening Google...")
            web.open_new("google.com")

        elif 'open gmail' in query:
            print("Please Wait...")
            speak("Opening Gmail...")
            web.open_new("gmail.com")

        elif 'open github' in query:
            print("Please Wait...")
            speak("Opening github...")
            web.open_new("github.com")

        elif 'open instagram' in query:
            print("Please Wait...")
            speak("Opening instagram...")
            web.open_new("instagram.com")

        elif 'open twitter' in query:
            print("Please Wait...")
            speak("Opening twitter...")
            web.open_new("twitter.com")

        elif 'open stack overflow' in query:
            print("Please Wait...")
            speak("Opening stackoverflow...")
            web.open_new("stackoverflow.com")

        elif 'play' in query:
            song = query.replace("play", "")
            print("Please Wait...")
            speak("Playing "+song)
            pywhatkit.playonyt(song)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Right now time is {strTime}")
            print(strTime)
        
        elif 'code' in query:
            codePath = "C:\\Users\\JAY JAGTAP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            print("Please Wait...")
            speak("Please Wait")
            os.startfile(codePath)

        elif 'date' in query:
            tod = datetime.date.today().strftime("%B %d %Y")
            print(tod)
            speak("Today's date is: "+tod)

        elif 'my location' in query:
            url = "https://www.google.com/maps/search/where+am+I+?/"
            web.get().open(url)
            speak("you must be somewhere near here, as per google maps")

        elif 'where am i' in query:
            url = "https://www.google.com/maps/search/where+am+I+?/"
            web.get().open(url)
            speak("you must be somewhere near here, as per google maps")

        elif 'locate' in query:
            speak("locating...")
            loc = query.replace("locate", "")
            if 'on map' in loc:
                loc = loc.replace("on map", "")
            url = "https://www.google.com/maps/place/"+loc+"/&amp;"
            web.get().open(url)
            print("here is the location of "+loc)
            speak("here is the location of "+loc)

        elif 'on map' in query:
            speak('locating ...')
            loc = query.split(" ")
            print(loc[1])
            url = 'https://google.nl/maps/place/'+loc[1] +'/&amp;'
            web.get().open(url)
            print('Here is the location of '+loc[1])
            speak('Here is the location of '+loc[1])

        elif 'where is' in query:
            speak("locating...")
            loc = query.replace("where is", "")
            if 'on map' in loc:
                loc = loc.replace("on map", "")
            url = "https://www.google.com/maps/place/"+loc+"/&amp;"
            web.get().open(url)
            print("here is the location of "+loc)
            speak("here is the location of "+loc)

        elif 'joke' in query:
            jok = pyjokes.get_joke()
            print(jok)
            speak(jok)
        
        elif 'funny' in query:
            jok = pyjokes.get_joke()
            print(jok)
            speak(jok)

        elif 'thank you' in query:
            print("your welcome")
            speak('your welcome')

        elif 'stop' in query:
            print('good bye, have a nice day!')
            speak('good bye, have a nice day!')
            sys.exit()

        elif 'quit' in query:
            print('good bye, have a nice day!')
            speak('good bye, have a nice day!')
            sys.exit()

     