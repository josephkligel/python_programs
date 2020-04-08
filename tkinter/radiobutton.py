from tkinter import *

def clicked():
    print("Clicked")

root = Tk()
v = IntVar()

Label(root, root.title("Options"), text="Choose a preferred language:",
justify=LEFT, padx=20).pack()

Radiobutton(root, text="Python", padx=20, variable=v, value=1, command=clicked).pack(anchor=W)
Radiobutton(root, text="C++", padx=20, variable=v, value=2, command=clicked).pack(anchor=W)

mainloop()
