import tkinter as Tk
from tkinter import *
import tkinter.font as TkFont
import pyttsx3


engine = pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()


root = Tk()

textv = StringVar()

font_path = "Python\zfont.ttf"  
custom_font = TkFont.Font(family="Outfit", size=20)  


obj = LabelFrame(root, text="Text to Speech", font="custom_font", bd=1)
obj.pack(fill="both", expand="yes", padx=20, pady=10)


lbl = Label(obj, text="➜", font=("Arial", 20))
lbl.pack(side=LEFT, padx=5)


entry = Entry(obj, textvariable=textv, font=("custom_font", 16), width=25, bd=5)
entry.pack(side=LEFT, padx=10)

btn = Button(obj, text="Speak", font=20, bg="Black", fg="white", command=speaknow)
btn.pack(side=LEFT, padx=10)


root.title("Text to Speech")
root.geometry("500x300")
root.resizable(False, False)


root.mainloop()
