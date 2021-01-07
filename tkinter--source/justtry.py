from tkinter import *
from tkinter import messagebox
window = Tk()

C = Canvas(window, bg="white", height=500, width=500)
#C.grid(row=2,column=3)
filename = PhotoImage(file = "boy22.png")
#C.create_image(20,20,anchor=NW,image=filename)
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
window.mainloop()