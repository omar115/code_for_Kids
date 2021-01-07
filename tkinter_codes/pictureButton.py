# importing only those functions 
# which are needed 
from tkinter import *
from tkinter.ttk import *

# creating tkinter window 
root = Tk() 
root.geometry('500x500')
# Adding widgets to the root window 
Label(root, text = 'Zabeer Hossain Omar', font =( 
'Verdana', 15)).pack(side = TOP, pady = 10) 

# Creating a photoimage object to use image 
photo = PhotoImage(file = r"/home/akash/git_workspace/code_for_Kids/tkinter_codes/circle.png") 

# Resizing image to fit on button 
photoimage = photo.subsample(10, 10) 

btn = Button(root, text = 'Click Me !', image = photoimage, compound = RIGHT, command = root.destroy)
btn.pack(side = TOP)

mainloop() 
