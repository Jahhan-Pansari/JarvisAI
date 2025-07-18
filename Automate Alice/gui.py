from tkinter import *
import os
import webbrowser
root = Tk()
root.title("Welcome to Operater")
root.geometry("500x500")
root.resizable(False, False)
with open("minecraftpath.txt", "r") as file:
    tlauncherpath = file.read() 
with open("blenderpath.txt", "r") as file:
    blenderpath = file.read()
with open("codepath.txt", "r") as file:
    codepath = file.read()
def opencode():
    os.startfile(codepath)
def openminecraft():
    os.startfile(tlauncherpath)
def openblender():
    os.startfile(blenderpath)


heading = Label(root, text="Welcome to PyOperater", font="bold")
heading.pack(side=TOP, anchor=CENTER)

button1 = Button(root, height=3, width=9, text="Visual Studio\nCode", command=opencode)
button1.pack(anchor=NW, padx=8)

button2 = Button(root, height=3, width=9, text="Minecraft", command=openminecraft)
button2.pack(anchor=NW, padx=8, pady=5)

button3 = Button(root, height=3, width=9, text="Blender", command=openblender)
button3.pack(anchor=NW, padx=8, pady=5)

root.mainloop()