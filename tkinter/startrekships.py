#!/usr/bin/python3
from tkinter import *
from tkinter import ttk

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        tab_control = ttk.Notebook(self)

        tab1 = ttk.Frame(tab_control)
        self.entD_photo = PhotoImage(file='/home/jkligel/Pictures/entD3.gif')
        content = """The Enterprise-D is a Galaxy-class ship and the fifth Federation starship
in the Star Trek universe to carry the name Enterprise.
Enterprise-D is the flagship of Starfleet.
The commanding officer is Captain Jean-Luc Picard for the majority of the ship\'s service."""
        lbl1 = Label(tab1, image=self.entD_photo).grid(column=1, row=0)
        lbl2 = Label(tab1, justify=LEFT, padx=10, text=content).grid(column=0, row=0)
        tab_control.add(tab1, text="Enterprise D")

        tab2 = ttk.Frame(tab_control)
        self.entC_photo = PhotoImage(file='/home/jkligel/Pictures/entC.gif')
        content2 = """The USS Enterprise (NCC-1701-C) was a 24th century Federation Ambassador-class starship operated by Starfleet.
It was the fourth Federation starship to bear the name Enterprise.
In 2344, Captain Rachel Garrett served as the ship's commanding officer."""
        lbl3 = Label(tab2, image=self.entC_photo).grid(column=1, row=0)
        lbl4 = Label(tab2, text=content2, justify=LEFT, padx=10).grid(column=0, row=0)
        tab_control.add(tab2, text="Enterprise C")

        tab_control.pack(expand=1, fill='both')

window = Window()
window.mainloop()
