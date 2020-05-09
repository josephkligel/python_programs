from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text="Hello World!", background="yellow").pack(side='left', anchor='nw')
ttk.Label(root, text="Hello World!", background="blue").pack(side='left', padx=10, pady=10)
ttk.Label(root, text="Hello World!", background="green").pack(side='left', ipady=10, ipadx=10)

for widget in root.pack_slaves():
    widget.pack_configure(fill=BOTH, expand=True)
    print(widget.pack_info())

label.pack_forget()
root.mainloop()
