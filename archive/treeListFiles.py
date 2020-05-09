from tkinter import *
from tkinter import ttk
import os

root = Tk()
treeview = ttk.Treeview(root)
treeview.pack()
treeview.column('#0', width='300')
treeview.heading('#0', text='Files', anchor='w')

def process_directory(parent, child):
    for item in os.listdir(child):
        abs_path = os.path.join(child, item)
        is_dir = os.path.isdir(abs_path)
        item_insert = treeview.insert(parent, 'end', text=item, open=1)
        if is_dir:
            process_directory(item_insert, abs_path)

top_path = '/home/jkligel/Downloads'
root_insert = treeview.insert('', 'end', text=top_path, open=1)
process_directory(root_insert, top_path)

def open_file():
    from tkinter import filedialog
    filename = filedialog.askdirectory()
    print(filename)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='Open', command=open_file)
menubar.add_cascade(label='File', menu=filemenu)
root.config(menu=menubar)

root.mainloop()
