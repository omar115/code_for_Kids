#importing all packages
import tkinter
from tkinter import *
from tkinter import messagebox
import webbrowser

#window part
window = tkinter.Tk()
window.title("Welcome to Food Order System\U0001f600")
window.geometry('500x500')

def fun():
    messagebox.showinfo("Menu ID", "1. Burger: OrderId1: 250tk"+"\n"+
                        "2. Sandwitch: OrderId2: 200tk"+"\n"+
                        "3. Pizza: OrderId3: 500tk")

btn1 = tkinter.Button(window, text="MenuList",bg="brown",font=('Arial',13), command=fun)
btn1.grid(column=0,row=0)

btn2 = tkinter.Button(window, text="OrderId1",bg="blue",font=('Arial',13))
btn2.grid(column=0,row=1)

btn3 = tkinter.Button(window, text="OrderId2",bg="blue",font=('Arial',13))
btn3.grid(column=0,row=2)

btn4 = tkinter.Button(window, text="OrderId3",bg="blue",font=('Arial',13))
btn4.grid(column=0,row=3)

label1 = tkinter.Label(window, text="Quantity")
label1.grid(column=1,row=1)

name = tkinter.StringVar()
entrybox = tkinter.Entry(window, width = 15, textvariable = name)
entrybox.grid(column=2,row=1)

btn5 = tkinter.Button(window, text="Confirm",bg="green",font=('Arial',10))
btn5.grid(column=3,row=1)

label2 = tkinter.Label(window, text="Quantity")
label2.grid(column=1,row=2)

name = tkinter.StringVar()
entrybox = tkinter.Entry(window, width = 15, textvariable = name)
entrybox.grid(column=2,row=2)

btn5 = tkinter.Button(window, text="Confirm",bg="green",font=('Arial',10))
btn5.grid(column=3,row=2)


btn9=tkinter.Button(window,text="Like us on facebook",bg="blue",font=("Arial",15))
btn9.grid(column=2,row=5)

def fun4(event):
    webbrowser.open_new_tab('https://www.youtube.com/')

btn9.bind('<Button-1>',fun4)

spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0,row=6)


window.mainloop()