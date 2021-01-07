#handling button click
#when you press button what will happen

import tkinter

#create a window
window = tkinter.Tk()

window.title("Welcome to Tkinter World :-)")

window.geometry('500x500')

label = tkinter.Label(window, text = "Hello Word!", font=("Arial Bold", 50))
label.grid(column=0, row=0)



def clicked():
    label.configure(text="button is clicked !!")

bton = tkinter.Button(window, text = "Click me",bg="orange",fg="red",command=clicked)
bton.grid(column=1, row=0)


#label.grid(column=0, row=0)
#this function calls the endless loop of the window,
#so the window will wait for any user interaction till we close it.
window.mainloop()