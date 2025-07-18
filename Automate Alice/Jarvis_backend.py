import os
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia    
import threading

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

emaildetailsDict = {
    "daksh" : "s.daksh.rathi@fountainheadschools.org",
    "vedant" : "s.vedant.dhameliya@fountainheadschools.org",
    "anant" : "s.anant.jain@fountainheadschools.org",
    "dhaval sir" : "s.dhaval.vagh@fountainheadschools.org",
    "shashank sir" : "s.shashank.ray@fountainheadschools.org",
    "tejas sir" : "s.tejas.gamit@fountainheadschools.org",
    "dhairya" : "s.dhairya.garg@fountainheadschools.org",
    "ipshita" : "s.ipsita.pansari@fountainheadschools.org",
    "mukund" : "s.mukund.chandak@fountainheadschools.org",
    "pankaj" : "pansaripankaj@gmail.com", 
    "parents of jahhan" : "p.jahhan.pansari@fountainheadschools.org",
    "self" : "s.jahhan.pansari@fountainheadschools.org",
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def sendMail(to, content):

    from email.message import EmailMessage
    import ssl
    import smtplib

    email_sender = 's.jahhan.pansari@fountainheadschools.org'
    email_password = 'lufrurrprhrbnojs'
    email_receiver = (to)
    subject = ("Email for you")
    body = (content)
    em = EmailMessage() 
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon! ")
    else:
        speak("Good Evening! ")
    speak("My name is Jarvis. How can I help you?")
def takeCommand2():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Recognizing...")
        try:
            query2 = r.recognize_google(audio, language='en-in')
            query2 = query2.lower()
            speak(query2)
            return query2
        except sr.UnknownValueError:
            print("Sorry, I didn't understand what you said. Please try again.")
            return takeCommand2()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening2...")
        audio = r.listen(source)
    try:
        print("Recognizing2...")
        query = r.recognize_google(audio, language='en-in')
        theanswer = (f"User said: {query}\n")
        print(theanswer)
        if 'quit' in query.lower():
            return None
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
def opengui(): 
    import tkinter as tk
    from PIL import Image, ImageTk

    root = tk.Tk()
    root.title("Animated GIF Player")
    root.overrideredirect(True)
    root.wm_attributes("-topmost", 1)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 375
    window_height = 150

    x_position = screen_width - window_width
    y_position = 0  

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    image = Image.open('Apple iOS11 Siri visual effect motion.png')
    image = image.resize((125, 125), Image.LANCZOS)
    display = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=display)
    label.pack(side=tk.LEFT, padx=10, pady=10)  

    global label_text
    label_text = tk.Label(root, text="Hey!\nHow can I help you", font=("Arial", 16, "bold"))
    label_text.pack(anchor="nw", padx=10, pady=22)
    
    root.mainloop()

x = 1
while x == 1:
    global label_text
    query2 = takeCommand2()
    if "jarvis" in query2:
        gui_thread = threading.Thread(target=opengui)
        gui_thread.start()
        speak("Hey!")
        try:
            query = takeCommand()
            if query is None:
                speak("Quiting Program, Thank you for using")
                label_text.config(text="Hey!\nQuiting Program")
                break
            elif 'quit' in query.lower():
                speak("Quiting Program, Thank you for using")
                label_text.config(text="Hey!\nQuiting Program")
                break
            elif 'bye' in query.lower():
                speak("Quiting Program, Thank you for using")
                label_text.config(text="Hey!\nQuiting Program")
                break
            elif 'wikipedia' in query.lower():
                speak("Searching Wikipedia...")
                query = query.replace("wikipeadia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'gmail' in query.lower():
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                label_text.config(text="Hey!\nOpening Gmail")
                speak("Opening Gmail")
                label_text.config(text="Hey!\nHow can I help you")
            elif 'open file manager' in query.lower():
                filemanagerpath = "C:\\Windows\\explorer.exe"
                os.startfile(filemanagerpath)
            elif 'open youtube' in query.lower():
                webbrowser.open_new_tab("https://www.youtube.com")
                label_text.config(text="Hey!\nOpening Youtube")
                speak("Opening YouTube")
                label_text.config(text="Hey!\nHow can I help you")
            elif 'open google' in query.lower():
                webbrowser.open("https://www.google.com")
                label_text.config(text="Hey!\nOpening google")
                speak("Opening")
                label_text.config(text="Hey!\nHow can I help you")
            elif 'open wikipedia' in query.lower():
                webbrowser.open_new_tab("https://en.wikipedia.org/")
                label_text.config(text="Hey!\nOpening Wikipedia")
                speak("Opening")
                label_text.config(text="Hey!\nHow can I help you")
            elif 'the time' in query.lower():
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is{strTime}")
            elif 'open car for sale' in query.lower():
                carforslaepath = "C:\\Users\\Admin\\Downloads\\Car.for.Sale.Simulator.2023.v0.2.3\\Car.for.Sale.Simulator.2023.v0.2.3\\Car.for.Sale.Simulator.2023.v0.2.3\\Car For Sale Simulator 2023.exe"
                label_text.config(text="Hey!\nOpening Car For Sale")
                os.startfile(carforslaepath)
                label_text.config(text="Hey!\nHow can I help you")
            elif 'open blender' in query.lower():
                blenderpath = "E:\\Blender\\blender-4.1....11-windows-x64\\blender.exe"
                label_text.config(text="Hey!\nOpening Blender")
                os.startfile(blenderpath)
                label_text.config(text="Hey!\nHow can I help you")
            elif 'open chrome' in query.lower():
                chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                label_text.config(text="Hey!\nOpening Chrome Browser")
                os.startfile(chromepath)
                label_text.config(text="Hey!\nHow can I help you")
            elif 'what is my name' in query.lower():
                label_text.config(text="Hey!\nJahhan Yogesh Pansari")
            elif 'file explorer' in query.lower():
                fileexplorerpath = "E:\\"
            elif 'send a mail' in query.lower():
                try:
                    speak("What would you like to say?")
                    label_text.config(text="Hey!\nSpeak Content to add in the mail")
                    content = takeCommand()
                    speak("Whom to share")
                    label_text.config(text="Hey!\nWhom to share speak the name")
                    whom_to_share_query = takeCommand()
                    notto = whom_to_share_query
                    to = emaildetailsDict[notto.lower()]
                    sendMail(to, content)
                    speak("Email has been sent!")
                    label_text.config(text="Hey!\n The mail has been Sent!!")
                except Exception as e:
                    print(e)
                    speak("Sorry, I couldn't send the email. Please try again.")
        except:
            speak("Sorry, I couldn't run the program. Please try again.")