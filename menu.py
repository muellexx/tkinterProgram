from tkinter import *
from tkinter import messagebox

def about(root):
    about_text = """
This program was written in order to show many different possibilities of the Python tkinter library.
Written by Muellex.
July 2020, Fukushima, Japan
"""
    response = messagebox.showinfo("About", about_text)
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
    helpmenu.add_command(label="About", command=lambda:about(root))
    menubar.add_cascade(label="Help", menu=helpmenu)
    return menubar
