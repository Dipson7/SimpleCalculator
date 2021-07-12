from _ast import Lambda
from tkinter import *

MyCal = Tk()
MyCal.configure(bg='black')

# Title of the project
MyCal.title('My Calculator')
MyCal.iconbitmap('C:/Users/dipso/OneDrive/Pictures/Softwarica/C.ico')

e = Entry(
    MyCal,
    width=20,
    borderwidth=5,
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    )
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))  # adding two strings


# equals to function

def button_equal():
    cal = str(e.get())  # store value of entry in cal
    total = eval(cal)  # runs the python which is passed as an argument
    e.delete(0, END)  # delete the value in entry
    e.insert(0, total)  # inserts the value in entry


def clear_but():
    e.delete(0, END)  # clears the entry in the screen


# Defining the buttons

button_1 = Button(
    MyCal,
    text='1',
    command=lambda: button_click(1),
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )
button_2 = Button(
    MyCal,
    text='2',
    command=lambda: button_click(2),
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )
button_3 = Button(
    MyCal,
    text='3',
    command=lambda: button_click(3),
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )
button_4 = Button(
    MyCal,
    text='4',
    command=lambda: button_click(4),
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_5 = Button(
    MyCal,
    text='5',
    command=lambda: button_click(5),
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_6 = Button(
    MyCal,
    text='6',
    command=lambda: button_click(6),
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_7 = Button(
    MyCal,
    text='7',
    command=lambda: button_click(7),
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_8 = Button(
    MyCal,
    text='8',
    command=lambda: button_click(8),
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_9 = Button(
    MyCal,
    text='9',
    command=lambda: button_click(9),
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_0 = Button(
    MyCal,
    text='0',
    command=lambda: button_click(0),
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_add = Button(
    MyCal,
    text='+',
    command=lambda: button_click('+'),
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_equal = Button(
    MyCal,
    text='=',
    command=button_equal,
    font=('georgia', 30),
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_clear = Button(
    MyCal,
    text='Reset',
    command=clear_but,
    font=('georgia', 20),
    width=3,
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_sub = Button(
    MyCal,
    text='-',
    command=lambda: button_click('-'),
    font=('georgia', 20),
    width=3,
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_mul = Button(
    MyCal,
    text='*',
    command=lambda: button_click('*'),
    font=('georgia', 20),
    width=3,
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_div = Button(
    MyCal,
    text='/',
    command=lambda : button_click('/'),
    font=('georgia', 20),
    width=3,
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_mod = Button(
    MyCal,
    text='Mod',
    command=lambda : button_click('%'),
    font=('georgia', 20),
    width=3,
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

button_power = Button(
    MyCal,
    text='^',
    command=lambda : button_click('**'),
    font=('georgia', 20),
    width=3,
    fg='lawn green',
    bg='black',
    activebackground='black',
    activeforeground='lawn green',
    bd=0,
    )

# Putting buttons on the screen

button_7.grid(row=2, column=2, ipadx=40, ipady=20)
button_8.grid(row=2, column=3, ipadx=40, ipady=20)
button_9.grid(row=3, column=0, ipadx=40, ipady=20)
button_4.grid(row=1, column=3, ipadx=40, ipady=20)
button_5.grid(row=2, column=0, ipadx=40, ipady=20)
button_6.grid(row=2, column=1, ipadx=40, ipady=20)
button_1.grid(row=1, column=0, ipadx=40, ipady=20)
button_2.grid(row=1, column=1, ipadx=40, ipady=20)
button_3.grid(row=1, column=2, ipadx=40, ipady=20)
button_0.grid(row=3, column=1, ipadx=40, ipady=20)
button_power.grid(row=3, column=3, ipadx=40, ipady=30)
button_add.grid(row=5, column=0, ipadx=40, ipady=20)
button_mod.grid(row=3, column=2, ipadx=40, ipady=30)
button_sub.grid(row=5, column=1, ipadx=40, ipady=30)
button_mul.grid(row=5, column=2, ipadx=40, ipady=30)
button_div.grid(row=5, column=3, ipadx=40, ipady=30)
button_clear.grid(row=6, column=0, columnspan=2, ipadx=110, ipady=20)
button_equal.grid(row=6, column=2, columnspan=2, ipadx=110, ipady=10)

mainloop()
