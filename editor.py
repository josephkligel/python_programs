from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
import sys

file_name = ''

class Editor(Tk):
    def __init__(self):
        super(Editor, self).__init__()
        self.title('Editor')
        self.geometry('640x480+50+50')

        self.textbox = Text(self, wrap='word')
        self.textbox.pack(fill='both', expand=True)
        self.create_menubar()
        self.create_bindings()

    def create_menubar(self):
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(menu=filemenu, label='File')
        
        filemenu.add_command(label='Open', command=self.open_file)
        filemenu.add_command(label='Save', command=self.save_file)
        filemenu.add_command(label='Save As', command=lambda: self.save_file(save_as=True))
        filemenu.entryconfig('Open', accelerator='Ctrl+O')
        filemenu.entryconfig('Save', accelerator='Ctrl+S')

        programmingmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(menu=programmingmenu, label='Programming')
        programmingmenu.add_command(label='C Template', command=lambda: self.template('C'))

        self.config(menu=menubar)

    def create_bindings(self):
        def select_all(event):
            event.widget.tag_add('sel', '1.0', 'end')

        self.bind('<Control-o>', self.open_file)
        self.bind('<Control-s>', self.save_file)
        self.bind_class('Text', '<Control-a>', select_all)

    def open_file(self, event=None):
        global file_name
        file_name = filedialog.askopenfile().name
        with open(file_name, 'r') as fr:
            for line in fr:
                self.textbox.insert('end', line)
        self.title(file_name)

    def save_file(self, event=None, save_as=False):
        if save_as:
            file_location = filedialog.asksaveasfilename()
            with open(file_location, 'w') as fh:
                for line in self.textbox.get('1.0', 'end'):
                    fh.write(line)
        else:
            save_dialog = messagebox.askyesno(title='Save Dialog', message='Are you sure you want to save?')
            if save_dialog:
                with open(file_name, 'w') as fh:
                    for line in self.textbox.get('1.0', 'end'):
                        fh.write(line)

    def template(self, language):
        if language == 'C':
            self.textbox.insert('1.0', """#include <stdio.h>\n
int main(int argc, int *argv[])\n
{\n
}""")
            #self.textbox.mark_set('insert', '2.4')# TODO
    
    def on_closing(self):
        print('closing')
        self.destroy()
    
    #self.protocol('WM_DELETE_WINDOW', self.on_closing)# TODO

if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()
