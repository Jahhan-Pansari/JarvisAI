import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import pyttsx3
import os
import speech_recognition as sr
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def on_dropdown_change(event):
    selected_option = dropdown.get()
    print(f'Selected option: {selected_option}')
    on_button_click()

with open("blenderpath.txt", "r") as file:
    blenderpath = file.read()
with open("codepath.txt", "r") as file:
    codepath = file.read()
with open("minecraftpath.txt", "r") as file:
    minecraftpath = file.read()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)
        print("Recognizing...")
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        therawanswer = (f"User said: {query}\n")
        theanswer = therawanswer.lower()
        print(theanswer)

        if "open youtube" in theanswer:
            webbrowser.open("youtube.com")
            speak("Opening youtube")
        elif "open google" in theanswer:
            webbrowser.open("google.com")
            speak("Opening Google")
        elif "open vscode" or "open vs code" in theanswer:
            os.startfile(codepath)
            speak("Opening Code")
        elif "search google" in theanswer:
            text_to_search = takeCommand()
            import re
            replaced_text_to_search = re.sub(r'\s', '+', query)
            part_1 = "https://www.google.com/search?q="
            last_part = "&safe=active&ssui=on"
            url = part_1 + replaced_text_to_search + last_part
            webbrowser.open(url)
        elif 'open pycharm' in query:
            codepath = "C:\\Program Files\\JetBrains\\PyCharm 2023.3.2\\bin\\pycharm64.exe"
            os.startfile(codepath)
        elif 'open blender' in query:
            blenderpath = "E:\\Blender\\blender-4.0.2-windows-x64\\blender.exe"
            os.startfile(blenderpath)
        elif 'open chrome' in query:
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
        elif 'play music' or 'play songs' in query:
            import random
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            randomchosensong = random.choice(songs)
            os.startfile(os.path.join(music_dir, randomchosensong))
    except Exception as e:
        print("Say that again please...")
        takeCommand()

root = tk.Tk()
root.geometry("250x250")
root.title("PyJarvis")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

def mainbutton():
    subprocess.run(["python", "Jarvis_backend.py"])

mainimage1 = tk.PhotoImage(file="jarvis.png")
mainbutton = tk.Button(root, image=mainimage1, command=mainbutton)
mainbutton.pack(side=tk.TOP, padx=5, pady=3)

def on_button_click():
    selected_option = dropdown.get()
    print(f'Selected option: {selected_option}')
    if selected_option == "Youtube":
        webbrowser.open("youtube.com")
        speak("Opening Youtube")
    if selected_option == "VS Code":
        os.startfile(codepath)
        speak("Opening VS Code")
    if selected_option == "Gmail":
        webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
        speak("Opening Gmail")
    if selected_option == "Google":
        webbrowser.open("google.com")
        speak("Opening Google")
    if selected_option == "Blender":
        os.startfile(blenderpath)
        speak("Opening Blender")
    if selected_option == "Google Calendar":
        webbrowser.open("calendar.googe.com")
        speak("Opening Google Calendar")
    if selected_option == "Docs":
        webbrowser.open("docs.google.com")
        speak("Opening Google Document")
    if selected_option == "Canva":
        webbrowser.open("canva.com")
        speak("Opening Canva")
    if selected_option == "Car for sale":
        os.startfile(r"C:\\Users\\Admin\\Downloads\\Car.for.Sale.Simulator.2023.v0.2.3\\Car.for.Sale.Simulator.2023.v0.2.3\\Car.for.Sale.Simulator.2023.v0.2.3\\Car For Sale Simulator 2023.exe")
        speak("Opening Car For Sale Simulator")
    if selected_option == "Minecraft":
        os.startfile(minecraftpath)
        speak("Opening Tlauncher")

button_frame = tk.Frame(root)
button_frame.pack()

def command1():
    subprocess.run(["python", "mailgui.py"])
def command2():
    subprocess.run(["python", "music.py"])
def command3():
    webbrowser.open("docs.google.com/document/u/0/?tgif=c")
    speak("Opening google docs")

image1 = tk.PhotoImage(file="Gmail_logo.png")
button1 = tk.Button(button_frame, image=image1, command=command1)
button1.pack(side=tk.LEFT, padx=5, pady=3)

image2 = tk.PhotoImage(file="music-player-img.png")
button2 = tk.Button(button_frame, image=image2, command=command2)
button2.pack(side=tk.LEFT, padx=5, pady=3)

image3 = tk.PhotoImage(file="Docs_logo.png")
button3 = tk.Button(button_frame, image=image3, command=command3)
button3.pack(side=tk.LEFT, padx=5, pady=3)

dropdown_options = ['Select One','Youtube', 'VS Code', 'Gmail', 'Google', 'Blender', 'Google Calendar', 'Canva', 'Docs', 'Car for sale', 'Minecraft']
dropdown = ttk.Combobox(frame, values=dropdown_options, state='readonly')
dropdown.bind('<<ComboboxSelected>>', on_dropdown_change)
dropdown.current(0)
dropdown.pack(side='bottom', pady=3)

root.mainloop()