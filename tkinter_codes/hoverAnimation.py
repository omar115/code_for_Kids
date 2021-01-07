from tkinter import *

root = Tk() 
root.geometry('500x500')

pic1 = PhotoImage(file='/home/akash/git_workspace/code_for_Kids/tkinter_codes/circle.png')
pic1 = pic1.subsample(10, 10) 
label = Label(root, image=pic1)
label.pack()

def change(e):
    pic2 = PhotoImage(file='/home/akash/git_workspace/code_for_Kids/tkinter_codes/icon.png')
    # pic2 = pic2.subsample(10,10)
    label.config(image=pic2)
    label.image = pic2

label.bind('<Enter>', change)

root.mainloop()