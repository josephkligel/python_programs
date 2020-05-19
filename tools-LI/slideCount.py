import os
import re
import zipfile
import tkinter
from tkinter import filedialog, messagebox

def show_error(text):
    tkinter.messagebox.showerror('Error', text)
def show_results(text):
    tkinter.messagebox.showinfo('Results', text)

def count(files):
    decks = {}
    results = ''
    for file in files:
        if os.path.abspath(file).endswith('.pptx'):
            decks[os.path.abspath(file)] = 0
        else:
            show_error(f'The file {file} in not a .pptx file and will be ignored.')
    for deck, count in sorted(decks.items()):
        try:
            archive = zipfile.ZipFile(deck, 'r')
            contents = archive.namelist()
        except Exception as e:
            show_error(f'Error reading {os.path.basename(deck)} ({e})')
        else:
            for fileEntry in contents:
                if(re.findall('ppt/slides/slide', fileEntry)):
                    decks[deck] += 1
    results += ('Slides\tDeck\n')
    for deck, count in sorted(decks.items()):
        results += (f'{count}\t{os.path.basename(deck)}\n')
    if (show_summary.get()):
        results += ('- - - - -\n')
        total = 0
        for count in decks.values():
            total += count
            results += f'{total} total slides in {len(decks)} decks.\n'
    show_results(results)

app = tkinter.Tk()
app.geometry('275x175')
app.title('SlideCount')

def clicked():
    t = tkinter.filedialog.askopenfilenames()
    count(t)

header = tkinter.Label(app, text='Welcome to SlideCount!', fg='blue', font=('Arial Bold', 16))
header.pack(side='top', ipady=10)

show_summary = tkinter.BooleanVar()
show_summary.set(True)
summary = tkinter.Checkbutton(app,text='Show Summary', var=show_summary)
summary.pack(ipady=10)

open_files = tkinter.Button(app, text='Choose decks...', command=clicked)
open_files.pack(side='bottom')

app.mainloop()
