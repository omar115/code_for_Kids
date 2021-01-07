import tkinter
from tkinter import messagebox


def fun():
    messagebox.showinfo("Important Message", "Order is Confirmed, price 100 tk")


window = tkinter.Tk()
window.title("Welcome to Tkinter World :-)")

button = tkinter.Button(window, text="Burger", command=fun)
button.pack()

window.mainloop()