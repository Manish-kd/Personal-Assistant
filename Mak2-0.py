#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
import time
import os
import webbrowser
from gtts import gTTS
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
    

#the keywords are - find, where is, crawl, video, search, open
def jarvis(data):
    if "how are you" in data:
        speak("I am fine")
        
    if "buy" in data:
        data = data.split(" ")
        buy = data[1:]
        buy  = ' '.join(map(str,buy))
        speak("Hold on manish, I am searcing "+buy+ " for you")
        url = "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+buy
        webbrowser.open_new(url)
        
    if "Who are you" in data:
        speak("I am Mak2.0")
        
    if "what is your name" in data:
        speak("I am Mak2.0")
        
    if "Chaos" in data:
        data = data.split(" ")
        chaos = data[1:]
        chaos = ' '.join(map(str,chaos))
        speak("Hold on Manish, I am searching"+chaos+"in chaos search engine")
        url = "http://localhost/webmining/tables.phcp?query="+chaos
        webbrowser.open_new(url)
 
    if "what time is it" in data:
        speak(ctime())
        
    if "find" in data:
        data  = data.split(" ")
        person = data[1:]
        person = ' '.join(map(str,person))
        speak("Hold on Manish, I will show you " + person )
        url = "http://www.facebook.com/search/top/?q=" + person
        webbrowser.open_new(url)
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Manish, I will show you where " + location + " is.")
        url = "https://www.google.nl/maps/place/" + location + "/&amp;"
        webbrowser.open_new(url)
    
    if "crawl" in data:
        data = data.split(" ")
        data = data[1:]
        data = ' '.join(map(str,data))
        speak("Crawling " + data)
        url = "http://localhost/webmining/mak2.php?query=" + data
        webbrowser.open_new(url)


    if "video" in data:
        data = data.split(" ")
        video = data[:-1]
        video1 = ' '.join(map(str, video))
        speak("Hold on Manish, I wil find you " + video1 )
        url = "https://www.youtube.com/results?search_query=" + video1
        webbrowser.open_new(url)
        
    if "search" in data:
        data = data.split(" ")
        search = data[1:]
        search1 = ' '.join(map(str, search))
        speak("Holdd on Manish, I am searching: " + search1)
        url = "https://www.google.co.in/search?q="+search1+"&aqs=chrome..69i57j0l5.1085j0j4&sourceid=chrome&ie=UTF-8"
        webbrowser.open_new(url)
        
    if "open" in data:
        data = data.split(" ")
        search = data[1:]
        search1 = ' '.join(map(str, search))
        speak("Holdd on Manish, I am searching: " + search1)
        url = "https://www."+search1
        webbrowser.open_new(url)
    
# initialization
time.sleep(2)
speak("Hi Manish, what can I do for you?")
while 1:
    data = recordAudio()
#    data = sys.stdin.readline("Ask user for something") 
    jarvis(data)