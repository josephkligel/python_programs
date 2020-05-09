from tkinter import *
from tkinter import ttk

class HelloApp(Tk):
    def __init__(self):
        super(HelloApp, self).__init__()
        self.label = ttk.Label(text='Hello, Tkinter!')
        self.label.grid(row=0, column=0, columnspan=2)
        ttk.Button(self, text='Texas', command=self.texas_hello).grid(row=1, column=0)
        ttk.Button(self, text='Hawaii', command=self.hawaii_hello).grid(row=1, column=1)
    def texas_hello(self):
        self.label.config(text='Howdy, Tkinter!')
    def hawaii_hello(self):
        self.label.config(text='Aloha, Tkinter!')

def main():
    root = HelloApp()
    root.mainloop()

if __name__ == '__main__':
    main()
