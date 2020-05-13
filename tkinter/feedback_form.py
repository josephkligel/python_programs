from tkinter import Tk, messagebox, Label, Button, Text, PhotoImage, END
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, master):
        super(App, self).__init__()

        logo = PhotoImage(file='/home/jkligel/python_programs/tkinter/Exercise_Files/Ch08/tour_logo.gif')
        label = Label(self, image=logo)
        label.grid(row=0, column=0, pady=10, padx=10)
        label.image = logo

        name_label = Label(self, text='Name:')
        self.name = ttk.Entry(self)
        name_label.grid(row=1, column=0)
        self.name.grid(row=1, column=1, sticky='w', pady=10, padx=10)

        email_label = Label(self, text='Email:')
        self.email = ttk.Entry(self)
        email_label.grid(row=2, column=0)
        self.email.grid(row=2, column=1, sticky='w', pady=10, padx=10)

        comment_label = Label(self, text='Comments:')
        self.comment = Text(self, width=70, height=5)
        comment_label.grid(row=3, column=0)
        self.comment.grid(row=3, column=1, stick='w', pady=10, padx=10)

        clear = Button(self, text='Clear', command=self.clear_action)
        clear.grid(row=4, column=0, sticky='e', pady=(10, 10), padx=10)
        submit = Button(self, text='Submit', command=self.submit_action)
        submit.grid(row=4, column=1, sticky='w', pady=(10, 10), padx=10)

        self.pack()

    def clear_action(self):
        self.name.delete(0, 'end')
        self.email.delete(0, 'end')
        self.comment.delete(1.0, 'end')

    def submit_action(self):
        print(self.name.get())
        print(self.email.get())
        print(self.comment.get(1.0, 'end'))
        messagebox.showinfo(title='Submit Success', message='Your feedback has been submitted.')
        self.clear_action()


def main():
    root = Tk()
    feedback = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
