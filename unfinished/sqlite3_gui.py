import sqlite3
from tkinter import ttk
from tkinter import Tk, Label, Button, Scrollbar

conn = sqlite3.Connection('sample.db')
cursor = conn.cursor()

def get_all_data():
    return cursor.execute('SELECT * FROM employees')
    # return cursor.fetchall()

column_names = [description[0] for description in get_all_data().description]

def delete_row(*args):
    cursor.execute('DELETE FROM employees WHERE id=?', (int(args[0][0])))# TODO:
    conn.commit()
    app.refresh(app.tab2)
    app.notebook.select(1)

def insert_row(*args):
    cursor.execute("INSERT INTO employees VALUES(?, ?, ?, ?, ?)", (args[0][0], args[0][1], args[0][2], args[0][3], args[0][4]))# TODO:
    conn.commit()
    app.refresh(app.tab2)
    app.notebook.select(1)

def update_row(*args):
    cursor.execute("UPDATE employees SET name=?, salary=?, department=?, position=? WHERE id=?", (name, salary, department, position, id))#TODO
    conn.commit()

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title('SQL Application')

        self.notebook = ttk.Notebook(self)
        self.notebook.pack()
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        # self.yScroll = Scrollbar(self.tab2, orient='vertically', command=self.tab2.yview)
        self.notebook.add(self.tab1, text='Record Manipulation')
        self.notebook.add(self.tab2, text='Table Records')

        self.create_components(self.tab1)

        self.create_table(self.tab2)

    def create_components(self, parent, horitzontal=0, row=None, column=None):
        def command():
            import re
            entryList = []
            for child in parent.winfo_children():
                child_name = str(child)
                if re.match('.*(!entry).*', child_name):
                    entryList.append(child.get())
            return entryList

        if horitzontal:
            for field in column_names:
                Label(parent, text=field.upper()+':').grid(row = row, column = column)
                ttk.Entry(parent, text='').grid(row=row+1, column=column)
                column += 1
            Button(parent, text='Delete', command=lambda: delete_row(command())).grid(row=row+2, column=0, pady=10)
            Button(parent, text='Update').grid(row=row+2, column=1, pady=10)
            Button(parent, text='Insert', command=lambda: insert_row(command())).grid(row=row+2, column=3, pady=10)
        else:
            row = 0
            column = 0
            for field in column_names:
                Label(parent, text=field.upper()+':').grid(row = row, column = column, padx=10, pady=10, sticky='e')
                ttk.Entry(parent, text='').grid(row=row, column=column+1, padx=10, pady=10)
                row += 1
            Button(parent, text='Delete', command=lambda: delete_row(command())).grid(row=row, column=0, pady=10)
            Button(parent, text='Update').grid(row=row, column=1, pady=10)
            Button(parent, text='Insert', command=lambda: insert_row(command())).grid(row=row, column=3, pady=10)

    def create_table_header(self, parent):
        row = 0
        column = 0
        for field in column_names:
            Label(parent, text=field.upper(), bg='#142E54', fg='white', relief='groove',
                font='lato 10 bold', borderwidth=2).grid(row=row, column=column, sticky='nsew', ipadx=10)
            column += 1

    def create_table(self, parent):
        #Create Table Header
        self.create_table_header(parent)
        #Create Table Body
        data = get_all_data()
        row = 1
        column = 0
        for data_row in data:
            for data_piece in data_row:
                Label(parent, text=data_piece, bg='#fff', fg='#000', borderwidth=2,
                    relief='groove', font='lato 10').grid(row=row, column=column, sticky='nsew')
                parent.columnconfigure(column, weight=1)
                column += 1
            column =0
            row += 1
        #Create Buttons for Tab2
        self.create_components(parent, horitzontal=1, row=row, column=column)

    def refresh(self, parent):
        for frame in parent.winfo_children():
            frame.destroy()
        self.create_table(parent)

if __name__ == '__main__':
    app = App()
    app.mainloop()

# conn.close()
# cursor.close()
