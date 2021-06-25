from tkinter import *
import sqlite3

root = Tk()

root.geometry('600x600')

database_name = '/home/akash/git_workspace/code_for_Kids/classWork/my_database.db'

c = sqlite3.connect(database_name)

cur = c.cursor() 

# cur.execute("""CREATE TABLE Library (
#         book_name text,
#         author_name text,
#         description text
#     )""")

# c.commit()

def fun():
    input_txt = txt1.get('1.0', 'end')
    print(input_txt)
    output = input_txt.split(',')
    
    book = str(output[0])
    author = str(output[1])
    description = str(output[2])
    # cur.execute("INSERT INTO Library VALUES ("+ str(output[0])+','+str(output[1])+','+str(output[2])+')')
    script = "INSERT INTO Library VALUES (?,?,?)"
    cur.execute(script, (book, author, description))

    c.commit()
    
    cur.execute("SELECT * FROM Library")
    c.commit()

    print(cur.fetchall())


txt1 = Text(root, height=5, width = 25, font='arial')
txt1.grid(row=0,column=0)

btn = Button(root, text='Add the Book', bd='5', command=fun)
btn.grid(row=1, column=0)

# c.close()
root.mainloop()