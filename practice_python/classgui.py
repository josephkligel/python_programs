from tkinter import *
from websitelist import websites
from os import *

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Website Selection Gui")
        Label(self, text="Sir or Mada\'am, what website would you like to go to?").grid(column=0, row=0)
        # self.minsize(500, 400)

        x, y = 1, 0
        for k,v in websites.items():

            lbl = self.create_label(x, y, k, v)
            btn = self.create_button(x, y, k, v)

            x += 1

    def create_label(self, x, y, k, v):
            lbl = Label(self, text=k)
            lbl.grid(column=y, row=x)
            return lbl

    def create_button(self, x, y, k, v):
        btn = Button(self, text=k[0], bg=v["color"])
        btn.grid(column=y+1, row=x)
        btn["command"] = lambda : self.clicked(v['url'])

        return btn

    def clicked(self, website='google.com'):
        expression = "google-chrome " + website
        return system(expression)

window = Window()
window.mainloop()
