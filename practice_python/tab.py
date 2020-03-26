from tkinter import *

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

    tab_control = self.Notebook(Window)
    tab1 = self.Frame(tab_control)
    tab2 = self.Frame(tab_control)

    tab_control.add(tab1, text="First Tab")
    tab_control.add(tab2, text="Second Tab")

window = Window()
window.mainloop()
