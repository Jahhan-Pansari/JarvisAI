from tkinter import *

def savevalues():
    with open("codepath.txt", "w") as code_file:
        codepathdata = codepathvalue.get()
        code_file.write(codepathdata)
    with open("blenderpath.txt", "w") as blender_file:
        blenderpathdata = blenderpathvalue.get()
        blender_file.write(blenderpathdata)
    with open("minecraftpath.txt", "w") as minecraft_file:
        minecraftpathdata = minecraftpathvalue.get()
        minecraft_file.write(minecraftpathdata)
    print("Data Saved!")

root = Tk()
root.geometry("244x135")
root.title("Setup Jarvis")
Label(root, text="Setup Jarvis", pady=12, font=("comicsansms", 13, "bold")).grid(row=0, column=3)

vscode_path = Label(root, text="VS-Code Path")
blender_path = Label(root, text="Blender")
minecraft_path = Label(root, text="Tlauncher")

vscode_path.grid(row=2, column=2, padx=2)
minecraft_path.grid(row=3, column=2, padx=2)
blender_path.grid(row=4, column=2, padx=2)


codepathvalue = StringVar()
blenderpathvalue = StringVar()
minecraftpathvalue = StringVar()

codeentry = Entry(root, textvariable=codepathvalue)
blenderentry = Entry(root, textvariable=blenderpathvalue)
minecraftentry = Entry(root, textvariable=minecraftpathvalue)

codeentry.grid(row=2, column=3,)
minecraftentry.grid(row=3, column=3)
blenderentry.grid(row=4, column=3,)

Button(text="Submit", command=savevalues).grid(row=7, column=3)

root.mainloop()