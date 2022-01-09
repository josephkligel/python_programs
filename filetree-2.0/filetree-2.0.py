from tkinter import ttk
from tkinter import Tk
from tkinter import filedialog, Menu, simpledialog, Button
import os, shutil

root_path = ''
class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title('File Browser')
        self.geometry("600x600")
        ttk.Style().theme_use("clam")

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.treeview = ttk.Treeview(self.main_frame)
        self.treeview.pack(side='left', fill='both', expand=True)
        self.treeview.heading('#0', text='List', anchor='w')
        self.menubar()
        self.buttons()

        self.yScroll = ttk.Scrollbar(self.main_frame, orient='vertical', command=self.treeview.yview)
        self.xScroll = ttk.Scrollbar(self.main_frame, orient='horizontal', command=self.treeview.xview)
        self.treeview.config(yscrollcommand=self.yScroll.set, xscrollcommand=self.xScroll.set)
        self.yScroll.pack(side='right', fill='y')
        # Uncomment below to add x-axis scrollbar
        # self.xScroll.pack(side='bottom', fill='x')
        selected = self.treeview.bind("<<TreeviewSelect>>", self.get_selection)

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
        button_frame = ttk.Frame(self)
        button_frame.pack()

        delete_button = Button(button_frame, text='Delete', command=self.delete_file)
        delete_button.grid(row=0, column=0, sticky='w', padx=5)
        move_button = Button(button_frame, text='Move', command=self.move_file)
        move_button.grid(row=0, column=1, sticky='w', padx=5)
        rename_button = Button(button_frame, text='Rename', command=self.rename_file)
        rename_button.grid(row=0, column=2, sticky='w', padx=5)
        copy_button = Button(button_frame, text='Copy File', command=self.copy_file)
        copy_button.grid(row=0, column=3, sticky='w', padx=5)

        open_button = Button(button_frame, text='Open Folder', command=self.initial_directory)
        open_button.grid(row=0, column=4, sticky='se', padx=5)
        open_button.config(bg='#116979', fg='white')

    def initial_directory(self):
        global root_path
        self.treeview.delete(*self.treeview.get_children())
        root_path = filedialog.askdirectory(mustexist=True, title="Double-click on folder you want to view and press OK.",
            initialdir='/home/jkligel/python_programs')
        root_insert = self.treeview.insert('', 'end', iid='root', text=root_path, open=1)
        self.process_directory(parent=root_insert, root_child_path=root_path)

    def process_directory(self, parent=None, root_child_path=root_path):
        if parent == None:
            self.treeview.delete(*self.treeview.get_children())
            parent = self.treeview.insert('', 'end', iid='root', text=root_child_path, open=1)
        for file in sorted(os.listdir(root_child_path)):
            abs_path = os.path.join(root_child_path, file)
            dir_boolean = os.path.isdir(abs_path)
            insert_file = self.treeview.insert(parent, 'end', abs_path, text=file, open=0)
            if dir_boolean:
                self.process_directory(insert_file, abs_path)

    def get_selection(self, event):
        return event.widget.selection()

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

    def delete_file(self):
        for selected_file in self.treeview.selection():
            os.remove(selected_file)
        parent_dir = os.path.dirname(selected_file)
        self.process_directory(root_child_path=parent_dir)

    def move_file(self):
        selected_files = self.treeview.selection()
        destination = filedialog.askdirectory(mustexist=True,
            title='Double-click to choose a destination.')
        for selected_file in selected_files:
            shutil.move(selected_file, destination)
        self.process_directory(root_child_path=destination)

    def rename_file(self):
        selected_file = self.treeview.selection()[0]
        parent_dir = os.path.dirname(selected_file)
        new_name = simpledialog.askstring('Input', 'What is the new name?', parent=self)
        os.rename(selected_file, os.path.join(parent_dir, new_name))
        self.process_directory(root_child_path=root_path)

    def copy_file(self):
        selected_files = self.treeview.selection()
        destination = filedialog.askdirectory(mustexist=True,
            title='Double-click to choose a destination.')
        for selected_file in selected_files:
            shutil.copy(selected_file, destination)
        self.process_directory(root_child_path=destination)

root = Window()
root.mainloop()
