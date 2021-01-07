import tkinter
from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("tutorial how to use images")
window.geometry("800x500")

my_img = ImageTk.PhotoImage(Image.open("thor.jpg"))
label = Label(image=my_img)
label.pack()


window.mainloop()