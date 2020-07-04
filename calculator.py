from tkinter import *

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_cl():
    e.delete(0, END)

def button_math(operation):
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = operation
    f_num = int(first_number)

def button_eq():
    second_number = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + int(second_number))
    elif math == "subtract":
        e.insert(0, f_num - int(second_number))
    elif math == "multiply":
        e.insert(0, f_num * int(second_number))
    elif math == "divide":
        e.insert(0, f_num / int(second_number))
    

def add_calculator(root):
    global e
    e = Entry(root, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


    button_1 = Button(root, text="1", width=10, pady=20, command=lambda: button_click(1))
    button_2 = Button(root, text="2", width=10, pady=20, command=lambda: button_click(2))
    button_3 = Button(root, text="3", width=10, pady=20, command=lambda: button_click(3))
    button_4 = Button(root, text="4", width=10, pady=20, command=lambda: button_click(4))
    button_5 = Button(root, text="5", width=10, pady=20, command=lambda: button_click(5))
    button_6 = Button(root, text="6", width=10, pady=20, command=lambda: button_click(6))
    button_7 = Button(root, text="7", width=10, pady=20, command=lambda: button_click(7))
    button_8 = Button(root, text="8", width=10, pady=20, command=lambda: button_click(8))
    button_9 = Button(root, text="9", width=10, pady=20, command=lambda: button_click(9))
    button_0 = Button(root, text="0", width=10, pady=20, command=lambda: button_click(0))
    button_add = Button(root, text="+", width=10, pady=20, command=lambda: button_math("add"))
    button_equal = Button(root, text="=", width=24, pady=20, command=lambda: button_eq())
    button_clear = Button(root, text="Clear", width=24, pady=20, command=lambda: button_cl())

    button_subtract = Button(root, text="-", width=10, pady=20, command=lambda: button_math("subtract"))
    button_multiply = Button(root, text="*", width=10, pady=20, command=lambda: button_math("multiply"))
    button_divide = Button(root, text="/", width=10, pady=20, command=lambda: button_math("divide"))


    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)
    button_0.grid(row=4, column=0)

    button_clear.grid(row=4, column=1, columnspan=2)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)


