from tkinter import *

root = Tk()
logo = PhotoImage(file='/home/jkligel/Pictures/entD.gif')
pane1 = Label(root, root.title('The Greatest Ship of All Time!!'), image=logo).pack(side='right')
content = """The Enterprise-D is a Galaxy-class ship and the fifth Federation starship
in the Star Trek universe to carry the name Enterprise.
Enterprise-D is the flagship of Starfleet.
The commanding officer is Captain Jean-Luc Picard for the majority of the ship\'s service."""
pane2 = Label(root, justify=LEFT, padx = 10, text=content).pack(side="left")

root.mainloop()
