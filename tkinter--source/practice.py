import tkinter

#create a window
window = tkinter.Tk()

window.title("Welcome to Tkinter World :-)")

window.geometry('500x500')

label = tkinter.Label(window, text = "Iron Man", font=("Arial Bold", 20))
label.grid(column=0, row=0)

bton = tkinter.Button(window,bg="red")
bton.grid(column=1, row=0)

label = tkinter.Label(window, text = "Batman", font=("Arial Bold", 20))
label.grid(column=0, row=1)

bton = tkinter.Button(window,bg="black")
bton.grid(column=1, row=1)



#label.grid(column=0, row=0)
#this function calls the endless loop of the window,
#so the window will wait for any user interaction till we close it.
window.mainloop()