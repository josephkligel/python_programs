import tkinter as tk
from tkinter import *

window = Tk()
btn = Button()
btn.pack()
btn["text"] = "Hello World"

def click():
    print("The button has been clicked.")
btn["command"] = click
window.mainloop() #needs to be last for the window to work and needs to be in place to open window
