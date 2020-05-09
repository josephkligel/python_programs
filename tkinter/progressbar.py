from tkinter import *
from tkinter import ttk

root = Tk()

progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progressbar.pack()
progressbar.config(mode='indeterminate')
progressbar.start()
progressbar.stop()
progressbar.config(mode='determinate', maximum=11.0, value=4.2)
progressbar.config(value=8.0)
progressbar.step()
value = DoubleVar()
progressbar.config(variable=value)

labelVar = StringVar()
def set_label(value):
    labelVar.set(value)

scale = ttk.Scale(root, orient=HORIZONTAL, length=400, variable=value, from_=0.0, to=11.0, command=set_label)
scale.set(4.2)
label = ttk.Label(root, textvariable=labelVar).pack()
scale.pack()

root.mainloop()
