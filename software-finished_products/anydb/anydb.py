from tkinter import Tk, StringVar, VERTICAL 
from tkinter import Label, Text, Entry, Canvas
from tkinter import Menu, filedialog
from tkinter import ttk
from glob import iglob
import os
import sqlite3
from sqlclass import Database

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title = 'Database Manager'
        self.geometry = '640x480+200+200'
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack()
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = Canvas(self.notebook)
        self.notebook.add(self.tab1, text='Tab 1')
        self.notebook.add(self.tab2, text='Tab 2')
        
        self.create_buttons(self.tab1)
        if os.path.exists('./last_database.log'):
            with open('./last_database.log', 'r') as fr:
                last_database = fr.readline().strip()
                try:
                    self.database_box.insert(1.0, last_database)
                    self.get_connection(last_database)
                except:
                    self.database_box.insert(1.0, '')

        #Last thing to do when initializing
        self.create_style()
    
    def create_menu(self):
        menubar = Menu(self)
        filemenu = Menu(menubar)
        self.config(menu=menubar)

    def create_buttons(self, parent):
        self.database_box = Text(parent, height=1)
        self.database_box.grid(row=0, column=0, padx=10, pady=10)
        openBtn = ttk.Button(parent, text='Choose Db')
        openBtn.grid(row=0, column=1, padx=10, pady=10, sticky='e')
        openBtn.config(command=self.choose_file)

        self.table_var = StringVar()
        self.combobox = ttk.Combobox(parent, textvariable=self.table_var)
        self.combobox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='we')
        self.populate_button = ttk.Button(parent, text='Populate Table',  command=lambda: self.populate_table(self.tab2, self.table_var.get()))
        self.populate_button.grid(row=2, column=1, padx=10, pady=10, sticky='e')

    def choose_file(self):
        database_dialog = filedialog.askopenfile(initialdir='./')
        self.database_box.insert(1.0, database_dialog.name)
        with open('last_database.log', 'w') as fh:
            fh.write(f'{database_dialog.name}\n')
        self.get_connection(database_dialog.name)

    def get_connection(self, database):
        self.db = Database(database)
        self.combobox.config(values=self.db.tables)            

    def populate_table(self, parent, table):
        self.all = self.db.get_all_data(table)
        self.column_names = [description[0] for description in self.all.description]
        #Create Header
        row, column = 0, 0
        for name in self.column_names:
            Label(parent, text=name, bg='#142E54', fg='white', relief='groove',
                font='lato 10 bold', borderwidth=1).grid(row=row, column=column, sticky='nsew')
            column += 1

        #Add rest of data
        row, column = 1, 0
        for data_row in self.all:
            for data_cell in data_row:
                cell = Entry(parent, borderwidth=2, relief='groove', font='lato 10')
                cell.grid(row=row, column=column, sticky='nsew')
                cell.insert(0, data_cell)
                cell.configure(state='readonly')
                column += 1
            row += 1
            column = 0

        #Add text entries and update, delete, and insert buttons
        crud_vars = []
        for i in range(len(self.column_names)):
            crud_var = StringVar()
            crud_vars.append(crud_var)
            Entry(parent, textvariable=crud_var).grid(row=row, column=i)
        
        def call_crud_vars(func):
            an_array = [var.get() for var in crud_vars]
            func(self.table_var.get(), an_array)
            self.refresh(parent)
            
        deleteBtn = ttk.Button(parent, text='Delete', command=lambda: call_crud_vars(self.db.delete_data))
        deleteBtn.grid(row=row+1, column=i-2, sticky='e')
        updateBtn = ttk.Button(parent, text='Update', command=lambda: call_crud_vars(self.db.update_data))
        updateBtn.grid(row=row+1, column=i-1, stick='e')
        insertBtn = ttk.Button(parent, text='Insert', command=lambda: call_crud_vars(self.db.insert_data))
        insertBtn.grid(row=row+1, column=i, sticky='e')

        self.notebook.select(1)

    def create_style(self):
        style = ttk.Style()
        style.configure('TButton', foreground='white', background='#142E54')

    def refresh(self, parent):
        for frame in parent.winfo_children():
            frame.destroy()
        self.populate_table(parent, self.table_var.get())

if __name__ == '__main__':
    app = App()
    app.mainloop()
