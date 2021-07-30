from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter

root = Tk()

root.geometry('1000x1000')

database_name = '/home/omar/git_workspace/code_for_Kids/classWork/my_database.db'      # write your location with database name

c = sqlite3.connect(database_name)      # connect with the database

cur = c.cursor()

# create the database

try:
    # create table in the database
    cur.execute("""CREATE TABLE book (
        book_name text,
        author_name text,
        date text
    )""")

except:
    print('database already created')

# function add where we will get text from the text box and apply string manipulation
def add():
    input_text = txt1.get('1.0','end')
    
    output_text = input_text.split(',')     #slice the string given from text box 1
    
    # assign the output into different variables
    book_name = output_text[0]
    author_name = output_text[1]
    date = output_text[2]

    '''
    placeholder is just a container you created before inserting a value into it.
    it helps us during the operation of sqlite database. using question mark (?) you can create
    a placeholder into it.
    '''

    script = 'INSERT INTO book VALUES (?,?,?)' # create a placeholder

    cur.execute(script, (book_name, author_name, date))     # adding value to the database

    c.commit()  # saving

    cur.execute('SELECT * FROM book')   # select all data from the database

    c.commit()  # saving

    print(cur.fetchall())   # using fetchall() you can pop out all the data from the database 
                            # and can show in terminal using print function


# function add where we will get text from the text box and apply string manipulation
def delete():
    input_text = txt2.get('1.0','end')
    
    book_name = input_text
    print(book_name)

    '''
    placeholder is just a container you created before inserting a value into it.
    it helps us during the operation of sqlite database. using question mark (?) you can create
    a placeholder into it.
    '''

    script = 'DELETE from book WHERE book_name = ?' # create a placeholder

    cur.execute(script, (book_name.strip(),))     # adding value to the database

    c.commit()  # saving

    cur.execute('SELECT * FROM book')   # select all data from the database

    # c.commit()  # saving

    print(cur.fetchall())   # using fetchall() you can pop out all the data from the database 
                            # and can show in terminal using print function


def update():
    input_text = txt3.get('1.0','end')
    input_text = input_text.strip()
    print('------- ',input_text)
    output_text = input_text.split(',')     #slice the string given from text box 1
    print(output_text)
    # assign the output into different variables
    
    date = output_text[0]
    book_name = output_text[1]

    script = 'UPDATE book SET date = (?) where book_name = (?)' # create a placeholder

    cur.execute(script, (date,book_name))     # adding value to the database

    c.commit()  # saving

    cur.execute('SELECT * FROM book')   # select all data from the database

    # c.commit()  # saving

    print(cur.fetchall())   # using fetchall() you can pop out all the data from the database 
                            # and can show in terminal using print function


def show_all():
    tree = ttk.Treeview(root, column=("column1","column2","column3"), show="headings")
    tree.heading("#1",text="Book Name")
    tree.heading("#2",text="Author Name")
    tree.heading("#3",text="Publication Date")
    tree.grid(row=0, column=5, pady=5)

    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()

    for i in rows:
        tree.insert("",tkinter.END, values=i)

# text 1 where user will write the book name, author name and description
txt1 = Text(root, height=5, width=25, font='arial')
txt1.grid(row=0, column=0, padx=10, pady=10)

# button to insert data into the database
btn1 = Button(root, text='Add the Book', bd=5, command=add)
btn1.grid(row=1, column=0, padx=10, pady=10)

# text 1 where user will write the book name, author name and description
txt2 = Text(root, height=5, width=25, font='arial')
txt2.grid(row=2, column=0, padx=10, pady=10)

# button to insert data into the database
btn2 = Button(root, text='Delete the Book', bd=5, command=delete)
btn2.grid(row=3, column=0, padx=10, pady=10)

txt3 = Text(root, height=5, width=25, font='arial')
txt3.grid(row=4, column=0, padx=10, pady=10)

# button to insert data into the database
btn3 = Button(root, text='Update the Book', bd=5, command=update)
btn3.grid(row=5, column=0, padx=10, pady=10)


btn4 = Button(root, text='Show Book List', bd=5, command=show_all)
btn4.grid(row=6, column=0, padx=20, pady=20)




root.mainloop()