
import os
import sys
import pyttsx3
import time
import json
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import numpy as np
import asyncio
import python_weather
from tkinter import *
from PIL import Image
from playsound import playsound
from datetime import datetime; get = datetime.now()

class Electron:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.engine.setProperty('rate', 198.5)
        self.wishAnyone()
        self.engine.say("This is electron! How can i help you ?")
        self.engine.runAndWait()
    #function to show strucutre of e-
    def what_is_your_name(self):
        self.speak("My name is Electron...A voice based assistant..")
    def e(self):
        self.window = Tk()
        self.window.title('Electron..')
        self.canvas = Canvas(self.window, width = 500, height = 500)
        self.canvas.pack()
        self.path = r"C:\Users\Lenovo\Documents\Sasikalyan\Project\electron\electron.gif"
        self.my_image = PhotoImage(file=self.path)
        self.canvas.create_image(0, 0, anchor = NW, image=self.my_image)
        self.text = "I'm Electron a voice based Assistant..\
                Elecron is in your service..."
        self.speak(self.text)
        self.window.mainloop()
    def speak(self, text):
        self.text = text
        self.engine.say(self.text)
        self.engine.runAndWait()
    #this function wish the user
    def wishAnyone(self):
        self.speak("Welcome back.....")
        self.format = get.hour
        if self.format >= 6 and self.format <12:
            self.engine.say("Good Morning ")
        elif self.format >= 12 and self.format < 16:
            self.engine.say("Good Afternoon ")
        elif self.format >= 16 and self.format < 21:
            self.engine.say("Good Evening ")
        else:
            self.engine.say("Good Night!")
        self.engine.runAndWait()
    #this function get the time
    def time(self):
        (self.h, self.m) = (get.hour, get.minute)
        self.string = "currently time is " + str(self.h) + "hours" + str(self.m) + "minutes"
        self.speak(self.string)
    #this function get the date
    def date(self):
        (self.y, self.m, self.d) = (get.year, get.month, get.day)
        self.string = "Today date is " + str(self.d) + " " + str(self.m) + " " + str(self.y)
        self.speak(self.string)
    #the function is used to get commmand from user
    def getCommand(self):
        print("Listening....")
        reco = sr.Recognizer()
        with sr.Microphone() as source:
            audio = reco.listen(source)
            path = r"C:\Users\Lenovo\Documents\Sasikalyan\Project\electron\.wav\quick.mp3"
            playsound(path)
        try:
            self.command = reco.recognize_google(audio)
            self.speak("You said " + str(self.command))
        except sr.UnknownValueError:
            self.speak("I did not get that ...speak again")
            return "none"
        except sr.RequestError as e:
            self.speak("Sorry I'm offline...Try again later")
            return "go offline"
        return str(self.command)
    #search engine
    def search_Wikipedia(self, data):
        self.data = data
        try:
            self.wikipage = wikipedia.page(self.data)
            self.speak("Here is the result...")
            self.speak(str(wikipedia.summary(self.data)))
            self.speak("Here are some useful links available ")
            self.link = str((self.wikipage.url))
            print(self.link)

        except:
            self.speak("No results found")
    #Google search / Chrome search
    def search_Microsoft_edge(self):
        self.speak("Connecting to Microsoft Edge...")
        try:
            self.speak("What you want to search?")
            search_for = str(self.getCommand().lower())
            webbrowser.open_new_tab(search_for + ".com")
        except webbrowser.Error:
            self.speak("could not locate runnable browser")
    #read news
    def read_News(self):
        query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "aea3985594904a2a946fa4bb7d2d07e1"
        }
        main_url = " https://newsapi.org/v1/articles"
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
        article = open_bbc_page["articles"]

        results = []

        for ar in article:
            results.append(ar["title"])
        for i in range(len(results)):
            print(i + 1, results[i])
        for topnews in results:
            self.speak(topnews)
    #playsongs
    def palySongs(self):
        self.songs_dir = r"C:\Users\Lenovo\Music\music"
        self.songs = os.listdir(self.songs_dir)
        os.startfile(os.path.join(self.songs_dir, self.songs[3]))
    #open images
    def openImages(self):
        self.speak("Wait a moment Opening Photos....")
        self.path = r"C:\Users\Lenovo\Pictures\images"
        self.images = os.listdir(self.path)
        os.startfile(os.path.join(self.path, self.images[0]))
        time.sleep(4)
    #function to take notes using voice
    def takeNotes(self):
        self.speak("I'm ready to take the notes....")
        path = r"D:\notes"
        print("                    List of files in Notes ")
        print("#################################################################")
        print(os.listdir(path))
        file_name = input("Enter the file name : ")
        while True:
            self.speak("Your turn...")
            cmd = str(self.getCommand().lower())
            if cmd == 'exit':
                break;
            else:
                file = str(file_name)+".txt"
                with open(os.path.join(path, file), 'a+') as fp:
                    fp.write(cmd+'\n')
        self.speak("Process Completed....")
    #Here my own chat bot integrated using the api of my chat bot
    def chat_with_me(self):
        self.speak("Wait a moment...i'm enabling chat bot")
        webbrowser.open("https://web-chat.global.assistant.watson.cloud.ibm.com/preview.html?region=eu-gb&integrationID=176cb3fd-5b65-4490-8633-ebf8b2520610&serviceInstanceID=33594e51-faeb-4809-9b9e-9bb16fcd8f08")
    async def getWeather_report(self):
        self.client = python_weather.Client(format=python_weather.IMPERIAL)
        self.speak("Enter location to get weather report...")
        self.location = input("Enter location : ")
        self.weather = await self.client.find(self.location)
        self.speak(self.weather.current.temperature)
        for forecast in self.weather.forecasts:
            print(str(forecast.date), forecast.sky_text, forecast.temperature)
            self.speak(str(forecast.date))
            self.speak(forecast.sky_text)
            self.speak(forecast.temperature)
        await self.client.close()
    def getLocation(self):
        self.speak("Wait a moment...Connecting to Google Maps..")
        webbrowser.open("https://www.google.com/maps")

if __name__ == '__main__':
    e = Electron()
    while True:
        cmd = e.getCommand().lower()
        if ('go offline' or "offline") in cmd:
            e.speak("logging out")
            exit(0)
        elif 'what is your name' in cmd:
            e.what_is_your_name()
        elif 'time' in cmd:
            e.time()
        elif 'date' in cmd:
            e.date()
        elif 'wikipedia' in cmd:
            e.speak("Wait a moment i'm connecting to Wikipedia")
            serachfor = input("Search here : ")
            e.speak("Searching results")
            e.search_Wikipedia(serachfor)
        elif 'search' in cmd:
            e.search_Microsoft_edge()
        elif ('read news' or 'news') in cmd:
            e.read_News()
        elif ('play songs' or 'songs') in cmd:
            e.palySongs()
        elif 'take notes' in cmd:
            e.takeNotes()
        elif ('open images' or 'show images' or 'images') in cmd:
            e.openImages()
        elif 'face' in cmd:
            e.e()
        elif ('chat' or 'chat with me') in cmd:
            e.chat_with_me()
        elif 'weather' in cmd:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(e.getWeather_report())
        elif ('my location' or 'get location') in cmd:
            e.getLocation()
        elif 'thank you' in cmd:
            e.speak("you are most welcome :)")
            print("You are most Welcome :)")
        elif 'game' in cmd:
            import AircraftGame.py
        #sleep for 10 sec
        time.sleep(3)
################################################################################
################################################################################
