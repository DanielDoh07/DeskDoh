import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime
import os
import pyaudio
import webbrowser
import smtplib



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(clip):
    engine.say(clip)
    engine.runAndWait()

def telljoke():
    speak(pyjokes.get_joke())

def time():
    pass


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

def furtherassistance():
    speak("Do you require further assistance")
    response = audiotranslate()
    if response == "yes" or response == "yeah":
        return 1
    elif response == "no":
        return 2
    else:
        speak("Sorry, I didn't quite catch that. Please say yes or no")
        furtherassistance()

def personSearch(name):
    pass

def sendEmail():
    serv = smtplib.SMTP("smtp.gmail.com")
    userlogin = input("Please input your user login in the following format: username@gmail.com")
    userpassword = input("Please input your email's password")
    sent_from = userlogin
    to

def openWEB(cmnd):
    cmnd = cmnd.lower()
    s = cmnd.find("open") + 5
    url = "www." + cmnd[s:] + ".com"
    webbrowser.open(url)


def main():
    f = open("emailf.txt", "a")
    f.write("Hello")
    f.close()
    f = open("emailf.txt")
    print(f.read())
    f.close()
    # while True:
    #     query = audiotranslate()
    #     print(query)
    #     if "quit" in query:
    #         speak("goodbye")
    #         break
    #     elif "stop" in query:
    #         speak("goodbye")
    #         break
    #     elif "bye" in query:
    #         speak("goodbye")
    #         break
    #     elif "open" in query:
    #         speak("on it")
    #         openWEB(query)
    #         if furtherassistance() == 1:
    #             pass
    #         else:
    #             break
    #     elif "who is" in query:
    #         speak("searching")
    #     elif "joke" in query:
    #         telljoke()
    #         speak("Would you like another joke?")







if __name__ == "__main__":
    main()