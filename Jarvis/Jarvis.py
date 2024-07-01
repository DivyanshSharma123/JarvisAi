import time
from turtle import listen
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyjokes
import smtplib
import pyautogui
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__=="__main__" :
    speak("Iron Man Tony Stark")


def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
          speak("Good Morning Sir")

     elif hour>=12 and hour<18:
          speak("Good Afternoon Sir")

     else:
          speak("Good Evening Sir")

     speak("My name is jarvis. How may i help you today?")

def takeCommand():

     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening...")
          r.pause_threshold = 1
          audio = r.listen(source)

     try:
          print("Recognizing....")
          query = r.recognize_google(audio, language= 'en-in')
          print(f"User said: {query}\n")

     except Exception as e:
          # print(e)
          print("Say that again please...")
          return "None"
     return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sharmadivyansh6611@gmail.com', 'Gmaill@6611')
    server.sendmail('sharmadivyansh6611@gmail.com', to, content)
    server.close()

if __name__=="__main__" :

    wishMe()
    while True:
    # if 1:
     query = takeCommand().lower()
            
     if 'wikipedia' in query:
         speak("Searching Wikipedia...")
         query = query.replace("wikipedia", " ")
         results= wikipedia.summary(query, sentences= 3)
         speak ("According to wikipedia")
         print(results)
         speak (results)

     elif 'go to sleep' in query:
         speak("Ok sir, You can call me anytime")
         break


     elif 'hello jarvis' in query:
         speak("Hello sir how are you")

     elif 'what is your name' in query:
         speak("My name is Jarvis Sir")

     elif 'how are you jarvis' in  query:
         speak ("I am fine sir. what about you?")

     elif 'i am good' in query:
         speak("That's great sir how can i assist you today?")

     elif 'open youtube' in query:
         webbrowser.open('youtube.com')
         speak("Opening Youtube sir")

     elif 'open google' in query:
         webbrowser.open('google.com')
         speak("Opening google sir")

     elif 'open facebook' in query:
         webbrowser.open('facebook.com')
         speak("Opening facebook sir")

     elif 'open gmail' in query:
         webbrowser.open('gmail.com')
         speak("Opening gmail sir")

     elif "open notepad" in query:
        subprocess.Popen(["notepad.exe"])
        speak("Opening Notepad for you sir")

     elif 'play music' in query:
         music_dir = 'D:\\Music\\Favourite Songs' 
         songs = os.listdir(music_dir)
         rd = random.choice(songs)
         print(songs)
         os.startfile(os.path.join(music_dir, rd))
         speak("Playing Music for you sir")


     elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir the time is {strTime}")


     elif 'open code' in query:
        codePath = "C:\\Users\\Divyansh Sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        speak("Opening Visual Studio Code Sir") 

     elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sharmadivyansh6611@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")    

     elif 'tell me a joke' in query:
         joke = pyjokes.get_joke()
         speak (joke)
     elif 'Shut down the system' in query:
         os.system("shutdown /s /t 5")
         speak("Shutting down the system for you sir")

     elif 'Restart the system' in query:
         os.system("shutdown /r /t 5")
         speak("Restarting the system sir")
    
     elif 'sleep the system' in query:
        
         os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
         speak("Sleep Mode activated sir")

     elif 'finally go to sleep' in query:
         speak("Going to sleep Sir... ")
         exit()