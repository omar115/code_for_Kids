#importing all packages
import tkinter
from tkinter import *
from tkinter import messagebox
import webbrowser

#window part
window = tkinter.Tk()
window.title("Welcome to Stem4Future Food System\U0001f600")
window.geometry('500x500')

#main part
#part-----1
def fun():
    messagebox.showinfo("Menu ID", "1. Burger: OrderId1: 250tk"+"\n\n"+
                        "2. Sandwitch: OrderId2: 200tk"+"\n\n"+
                        "3. Sub: OrderId3: 150tk")
    
btn1 = tkinter.Button(window, text="MenuList",bg="brown",font=("Arial",13), command=fun)
btn1.grid(column = 0, row = 0)

#part----2
btn2 = tkinter.Button(window, text="OrderId:1",bg="White",fg="black",font=("Arial",12))
btn2.grid(column=0,row=1)

btn3 = tkinter.Button(window, text="OrderId:2",bg="White",fg="black",font=("Arial",12))
btn3.grid(column=0,row=2)

btn4 = tkinter.Button(window, text="OrderId:3",bg="White",fg="black",font=("Arial",12))
btn4.grid(column=0,row=3)




#part----3
label1 = tkinter.Label(window, text = "Quantity")
label1.grid(column = 1, row = 1)

name = tkinter.StringVar()
entrybox = tkinter.Entry(window, width = 15, textvariable = name)
entrybox.grid(column = 2, row = 1)


btn6 = tkinter.Button(window, text="Confirm",bg="magenta",fg="black",font=("Arial",7))
btn6.grid(column=3,row=1)




#similar task for other buttons
label2 = tkinter.Label(window, text = "Quantity")
label2.grid(column = 1, row = 2)

name = tkinter.StringVar()
nameEntered = tkinter.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 2, row = 2)

btn6 = tkinter.Button(window, text="Confirm",bg="purple",fg="black",font=("Arial",7))
btn6.grid(column=3,row=2)

#the last option

label3 = tkinter.Label(window, text = "Quantity")
label3.grid(column = 1, row = 3)

name = tkinter.StringVar()
nameEntered = tkinter.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 2, row = 3)

    
btn7 = tkinter.Button(window, text="Confirm",bg="yellow",fg="black",font=("Arial",7))
btn7.grid(column=3,row=3)

#finalizing---everythin
#last--part

btn8 = tkinter.Button(window, text="Total",bg="green",fg="black",font=("Arial",20))
btn8.grid(column=0,row=4)


btn9=tkinter.Button(window,text="Like us on facebook",bg="blue",font=("Arial",15))
btn9.grid(column=2,row=5)

def facebook(event):
    webbrowser.open_new_tab('https://www.facebook.com/STEM4Future')

btn9.bind('<Button-1>',facebook)

window.mainloop()
