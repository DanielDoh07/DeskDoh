import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime
import os
import pyaudio
import youtube_dl #yt
import webbrowser


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(clip):
    engine.say(clip)
    engine.runAndWait()

def audiotranslate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=.5)
        print("Listening...")
        audio = r.listen(source)
    try:
        cmnd = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Sorry, I didn't quite catch that")
        cmnd = audiotranslate()
        cmnd = cmnd.lower()
    return cmnd

def personSearch(name):
    pass

def sendEmail():
    pass

def openWEB(cmnd):
    cmnd = cmnd.lower()
    s = cmnd.find("open") + 5
    url = "www." + cmnd[s:] + ".com"
    webbrowser.open(url)



while True:
    query = audiotranslate()
    print(query)
    if "quit" in query:
        speak("ok")
        break
    elif "stop" in query:
        speak("ok")
        break
    elif "open" in query:
        speak("on it")
        print(openWEB(query))
    elif "who is" in query:
        speak("searching")




# def main():
#     run = True
#     while run == True:
#         query = audiotranslate()
#         if "stop" or "thanks" or "bye" or "quit" in query:
#             print(query)
#             run == False
#         elif "open youtube" in query:
#             speak("Opening youtube")



# if __name__ == "__main__":
#     main()