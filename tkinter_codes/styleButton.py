from tkinter import *
from tkinter.ttk import *

root = Tk()

root.geometry('500x500')

styl = Style()

styl.configure('TButton', font = ('arial', 30, 'bold', 'underline', 'italic'), fg = 'red')

btn = Button(root, text='Click Me!', styl='TButton', command=root.destroy)

btn.pack()

root.mainloop()