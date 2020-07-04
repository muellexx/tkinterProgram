from tkinter import *
from tkinter import messagebox

def info(root):
    response = messagebox.showinfo("This is my Popup!", "Hello World!")
    Label(root, text=response).pack()

def add_menu(root):
    global menubar
    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New")
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Save")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help")
    helpmenu.add_command(label="About", command=lambda:info(root))
    menubar.add_cascade(label="Help", menu=helpmenu)
    return menubar
