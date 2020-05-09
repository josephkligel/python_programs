# coding: utf-8
from tkinter import *
from tkinter import ttk
root = Tk()
label = ttk.Label(root, text='Hello, Tkinter')
label.pack()
label.config(text='Howdy, Tkinter!')
label.config(wraplength=150)
label.config(justify=CENTER)
label.config(foreground='blue', background='yellow')
label.config(font=['Courier', 18, 'bold'])
logo = PhotoImage(file='./Exercise_Files/Ch03/python_logo.gif')
label.config(image=logo)
#label.config(compound='text')
label.config(compound='top')
label.img = logo
label.config(image=label.img)
root.mainloop()
