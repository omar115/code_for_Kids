from tkinter import *
import sqlite3

database_name = '/home/akash/git_workspace/code_for_Kids/classWork/my_database.db'
# name = 'customer.db'    # .db is the extention of database

c = sqlite3.connect(database_name)

cur = c.cursor() 

root = Tk()

root.geometry('500x500')

def fun():
    
    cur.execute("INSERT INTO customers VALUES ('Mahbub A','Alam','ma.Alam@gmail.com')")
    c.commit()
    c.close()
    # cur.execute

btn = Button(root, text='Click Me!', bd='5', command=fun)

btn.grid(row=0,column=0)

# label = Label(root,text='blank')
label = Text(root, height=5, width = 15, font='arial')
label.grid(row=1, column=0)

root.mainloop()