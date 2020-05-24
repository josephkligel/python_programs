from tkinter import Tk, StringVar, VERTICAL 
from tkinter import Label, Text, Entry, Canvas
from tkinter import Menu, filedialog
from tkinter import ttk
from glob import iglob
import sqlite3

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

        #yscroll = ttk.Scrollbar(self.tab2, orient=VERTICAL, command=self.tab2.yview)
        #self.tab2.config(yscrollcommand=yscroll.set)
        #yscroll.grid(row=0, column=20, sticky='ns')
        #self.tab2.columnconfigure(20, weight=1)

    def create_menu(self):
        menubar = Menu(self)
        filemenu = Menu(menubar)
        self.config(menu=menubar)

    def create_buttons(self, parent):
        self.database = Label(parent)
        self.database.grid(row=0, column=0)
        openBtn = ttk.Button(parent, text='Choose Db')
        openBtn.grid(row=0, column=1)
        openBtn.config(command=self.choose_file)

        self.table_name = StringVar()
        self.combobox = ttk.Combobox(parent, textvariable=self.table_name)
        self.combobox.grid(row=1, column=0, columnspan=2)
        self.populate_button = ttk.Button(parent, text='Populate Table',  command=lambda: self.populate_table(self.tab2, self.table_name.get()))
        self.populate_button.grid(row=2, column=1, sticky='e')

    def choose_file(self):
        database = filedialog.askopenfile(initialdir='./')
        self.database.config(text=database.name)
        self.get_connection(self.tab1, database.name)

    def get_connection(self, parent, database):
        self.conn = sqlite3.Connection(database)
        self.cursor = self.conn.cursor()
        get_tables_statement = self.cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
        tables = []
        for name in get_tables_statement:
            tables.append(name[0])
        self.combobox.config(values=tables)
        #try :
           # self.combobox.bind('<<ComboboxSelected>>', lambda e: self.populate_table(self.tab2, self.table_name.get()))
        #except sqlite3.OperationalError as oe:
         #   print('Could not retrieve table name')

    def populate_table(self, parent, table):
        self.get_all_data = self.cursor.execute(f'SELECT * FROM {table}')
        self.column_names = [description[0] for description in self.get_all_data.description]
        
        #Create Header
        row, column = 0, 0
        for name in self.column_names:
            Label(parent, bg='#142E54', text=name, fg='white', relief='groove',
                font='lato 10 bold', borderwidth=2).grid(row=row, column=column, sticky='nsew')
            column += 1

        #Add rest of data
        row, column = 1, 0
        for data_row in self.get_all_data:
            for data_cell in data_row:
                cell = Entry(parent, bg="White", fg="Black", borderwidth=2, relief='groove', font='lato 10')
                cell.grid(row=row, column=column, sticky='nsew')
                cell.insert(0, data_cell)
                cell.configure(state='readonly')
                column += 1
            row += 1
            column = 0


if __name__ == '__main__':
    app = App()
    app.mainloop()
