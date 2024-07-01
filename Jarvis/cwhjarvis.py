import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import smtplib
import os
import subprocess
import random

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=1, phrase_time_limit=5)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%A, %B %d, %Y")

def send_email(to_address, subject, message):
    from_address = "sharmadivyansh6611@gmail.com"
    password = "gmail@6611"
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_address, password)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(from_address, to_address, email_message)
        speak("Email sent successfully.")
    except Exception as e:
        speak(f"Failed to send email: {str(e)}")

def open_website(url):
    webbrowser.open(url)

def open_application(path):
    os.startfile(path)

def play_music(directory):
     music_dir = 'D:\\Music\\Favourite Songs' 
     songs = os.listdir(music_dir)
     rd = random.choice(songs)
     print(songs)
     os.startfile(os.path.join(music_dir, rd))

if __name__ == "__main__":
    speak("How can I assist you today?")
    while True:
        command = listen()
        if command:
            if "your name" in command:
                speak("My name is Jarvis.")
            elif "day is today" in command:
                speak(f"Today is {get_date()}.")
            elif "time is it" in command:
                speak(f"The time is {get_time()}.")
            elif "send email" in command:
                speak("What is the recipient's email address?")
                to_address = listen()
                speak("What is the subject?")
                subject = listen()
                speak("What is the message?")
                message = listen()
                send_email(to_address, subject, message)
            elif "open youtube" in command:
                open_website("https://www.youtube.com")
            elif "open google" in command:
                open_website("https://www.google.com")
            elif "open facebook" in command:
                open_website("https://www.facebook.com")
            elif "open notepad" in command:
                subprocess.Popen(["notepad.exe"])
            elif "play music" in command:
                music_directory = "C:\\Path\\To\\Your\\Music\\Directory"
                play_music(music_directory)
            elif "open visual studio code" in command:
                open_application("C:\\Path\\To\\Visual Studio Code\\Code.exe")
            elif "exit" in command or "stop" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I did not understand that command.")