from tkinter import ttk
from tkinter import Tk, Menu

gitList = [
    'bash',
    'blog',
    'budgetCrud',
    'config',
    'c_programs',
    'cv',
    'Programmapedia',
    'python_programs',
    'Wiki-API'
]

class App(Tk):
    global gitList
    def __init__(self):
        super(App, self).__init__()
        self.title('Installer Gui')
        # self.geometry("600x600")
        self.create_menus()

        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)
        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)
        tab3 = ttk.Frame(notebook)
        notebook.add(tab1, text='Required')
        notebook.add(tab2, text='Github Programs')
        notebook.add(tab3, text='Help')
        notebook.select(1)

        self.create_buttons(tab2)

    def create_menus(self):# TODO: Finish this
        menubar = Menu(self)
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        self.config(menu=menubar)


    def create_buttons(self, parent, button_text='Click Here', command=None):
        # parent.columnconfigure(0, weight=1)
        # parent.columnconfigure(1, weight=1)
        for i in range(0, len(gitList)):
            # parent.rowconfigure(i, weight=1)
            label = ttk.Label(parent, text=gitList[i]+':')
            label.grid(row=i, column=0, sticky='e', padx=10)

            if command == None:
                command = f'git clone https://github.com/zigjag/{gitList[i]}.git'

            button = ttk.Button(parent, text=button_text, command=lambda: self.system_command(command))
            button.grid(row=i, column=1, pady=5)

    def system_command(self, command):# TODO: Add a way to auto install programs for user
        import os
        os.system(f'{command}')

app = App()
app.mainloop()
