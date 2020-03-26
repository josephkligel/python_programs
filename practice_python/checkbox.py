from tkinter import *

root = Tk()

def var_states():
    print("Warrior: %d,\nMage: %d" % (var1.get(), var2.get()))

Label(root, root.title("Adventure Game"),
text=">>>>>>>>>>>Your Adventure Role<<<<<<<<<<<").grid(row=0, sticky=N)

var1=IntVar()
Checkbutton(root, text="Warrior", variable=var1).grid(row=1, sticky=W)

var2=IntVar()
Checkbutton(root, text="Mage", variable=var2).grid(row=2, sticky=W)

Button(root, text='Quit', command=root.destroy).grid(row=3, sticky=W, pady=4)

Button(root, text='Show', command=var_states).grid(row=3, sticky=E, pady=4)

mainloop()
