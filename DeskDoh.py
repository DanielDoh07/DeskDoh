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


class DeskDoh:

    def __init__(self, engine=pyttsx3.init("sapi5")):
        self.engine = engine
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)
        self.username = ""
        self.password = ""

    def speak(self, clip):
        self.engine.say(clip)
        self.engine.runAndWait()

    def tell_joke(self):
        self.speak(pyjokes.get_joke())

    def time(self):
        pass

    def audio_translate(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=.5)
            print("Listening...")
            audio = r.listen(source)
        try:
            cmnd = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I didn't quite catch that")
            cmnd = self.audio_translate()
            cmnd = cmnd.lower()
        return cmnd

    def further_assistance(self):
        self.speak("Do you require further assistance")
        response = self.audio_translate()
        if response == "yes" or response == "yeah":
            return 1
        elif response == "no":
            return 2
        else:
            self.speak("Sorry, I didn't quite catch that. Please say yes or no")
            self.further_assistance()

    def personSearch(name):
        pass

    def input_info(self):
        serv = smtplib.SMTP("smtp.gmail.com")
        self.username = input("Please input your user login in the following format: username@gmail.com")
        self.password = input("Please input your email's password")
        sent_from = self.username

    def sendEmail(self):
        if len(self.username) and len(self.password) > 0:

        else:
            self.input_info()

        f = open("emailf.txt", "a")
        f.write("Hello")
        f.close()
        f = open("emailf.txt")
        print(f.read())
        f.close()



    def openWEB(self, cmnd):
        cmnd = cmnd.lower()
        s = cmnd.find("open") + 5
        url = "www." + cmnd[s:] + ".com"
        webbrowser.open(url)

    def runDesk(self):
        while True:
            query = self.audio_translate()
            print(query)
            if "quit" in query:
                self.speak("goodbye")
                break
            elif "stop" in query:
                self.speak("goodbye")
                break
            elif "bye" in query:
                self.speak("goodbye")
                break
            elif "open" in query:
                self.speak("on it")
                self.openWEB(query)
                if self.further_assistance() == 1:
                    pass
                else:
                    break
            elif "who is" in query:
                self.speak("searching")
            elif "joke" in query:
                self.tell_joke()
                self.speak("Would you like another joke?")


if __name__ == "__main__":
    j = DeskDoh()
    j.runDesk()

