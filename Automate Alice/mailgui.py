from tkinter import *
import webbrowser
import pyttsx3
root = Tk()
root.title("Choose an option")
root.geometry("200x100")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def button1():
    webbrowser.open("https://mail.google.com/mail/u/1/#inbox?compose=new")
    speak("Opening Gmail Compose ")
    root.destroy()

def button2():
    webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
    speak("Opening Gmail")
    root.destroy()

button1 = Button(root, text="Compose a mail", height=3, command=button1)
button1.pack(side=TOP, fill='x')

button2 = Button(root, text="Open Gmail", height=3, command=button2)
button2.pack(side=BOTTOM, fill='x')

root.mainloop()