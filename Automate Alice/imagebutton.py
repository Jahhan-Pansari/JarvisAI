from tkinter import *
root = Tk()
root.geometry("300x300")
root.title("PyJarvis")

image_file = "Gmail_logo.png"
image = PhotoImage(file=image_file)

button1 = Button(root, image=image)
button1.pack()

root.mainloop()