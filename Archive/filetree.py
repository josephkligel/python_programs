from tkinter import ttk
from tkinter import Tk
from tkinter import filedialog, Menu
import os

root_path = ''
class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title('File Browser')
        self.geometry("600x600")
        ttk.Style().theme_use("clam")

        self.treeview = ttk.Treeview(self)
        self.treeview.pack(fill='both', expand=True)
        self.treeview.heading('#0', text='List', anchor='w')
        self.menubar()
        self.buttons()

        self.yScroll = ttk.Scrollbar(self.treeview, orient='vertical', command=self.treeview.yview)
        self.xScroll = ttk.Scrollbar(self.treeview, orient='horizontal', command=self.treeview.xview)
        self.treeview.config(yscrollcommand=self.yScroll.set, xscrollcommand=self.xScroll.set)
        self.yScroll.pack(side='right', fill='y')
        # Uncomment below to add x-axis scrollbar
        # self.xScroll.pack(side='bottom', fill='x')
        self.treeview.bind("<<TreeviewSelect>>", self.get_selection)

    def menubar(self):
        menubar = Menu(self)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label='Open', command=self.initial_directory)
        menubar.add_cascade(label='File', menu=file_menu)

        print_menu = Menu(menubar, tearoff=0)
        print_menu.add_command(label='Text', command=self.print_to_text)
        menubar.add_cascade(label="Print", menu=print_menu)

        self.config(menu=menubar)

    def buttons(self):
        open_button = ttk.Button(self.treeview, text='Open Folder', command=self.initial_directory)
        open_button.pack(side="bottom", anchor='se')

    def initial_directory(self):
        global root_path
        root_path = filedialog.askdirectory(mustexist=True, title="Double-click on folder you want to view and press OK.")
        root_insert = self.treeview.insert('', 'end', iid='root', text=root_path, open=1)
        self.process_directory(root_insert, root_path)

    def process_directory(self, parent, root_child_path):
        for file in os.listdir(root_child_path):
            abs_path = os.path.join(root_child_path, file)
            dir_boolean = os.path.isdir(abs_path)
            insert_file = self.treeview.insert(parent, 'end', abs_path, text=file, open=0)
            if dir_boolean:
                self.process_directory(insert_file, abs_path)

    def get_selection(self, event):
        return print(next(iter((self.treeview.selection()))))

    def print_to_text(self):
        with open('file-list.txt', 'w') as fh:
            fh.write(root_path+'\n')

            for file in os.listdir(root_path):
                abs_path = os.path.join(root_path, file)
                if os.path.isdir(abs_path):
                    fh.write(f'  >{file}\n')
                    for subfile in os.listdir(abs_path):
                        fh.write(f'\t\t\t{subfile}\n')
                else:
                    fh.write(f'\t{file}\n')

root = Window()
root.mainloop()
