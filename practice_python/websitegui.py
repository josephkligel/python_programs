from tkinter import *
from os import *

def clicked():
    system("google-chrome")
    exit()

def click(url):
    system("google-chrome " + url)
    exit()

window = Tk()

lbl1 = Label(window, text="Google")
lbl1.grid(column = 0, row = 0)
btn1 = Button(text="G", bg="green")
btn1.grid(column = 1, row = 0)
btn1["command"] = lambda : click('google.com')

lbl2 = Label(window, text="Yahoo")
lbl2.grid(column = 0, row = 1)
btn2 = Button(text="Y!", command=clicked, bg="purple")
btn2.grid(column = 1, row = 1)

lbl3 = Label(window, text="Reddit")
lbl3.grid(row = 2, column = 0)
btn3 = Button(text="Rd", command=clicked, bg="red")
btn3.grid(row = 2, column = 1)

window.mainloop()
