from tkinter import *
import sqlite3

root = Tk()

root.geometry('600x600')

database_name = '/home/akash/git_workspace/code_for_Kids/classWork/my_database.db'

c = sqlite3.connect(database_name)

cur = c.cursor()

# create the database

try:
    
    cur.execute("""CREATE TABLE book (
        book_name text,
        author_name text,
        date text
    )""")

except:
    print('database already created')


def add():
    input_text = txt1.get('1.0','end')
    # print(input_text)
    output_text = input_text.split(',')
    # print(output_text)

    book_name = output_text[0]
    author_name = output_text[1]
    date = output_text[2]

    script = 'INSERT INTO book VALUES (?,?,?)' # create a placeholder

    cur.execute(script, (book_name, author_name, date))

    c.commit()

    cur.execute('SELECT * FROM book')

    c.commit()

    print(cur.fetchall())






txt1 = Text(root, height=5, width=25, font='arial')
txt1.grid(row=0, column=0)

btn = Button(root, text='Add the Book', bd=5, command=add)
btn.grid(row=1, column=0)

root.mainloop()