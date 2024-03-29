from tkinter import *
import sqlite3

root = Tk()

root.geometry('600x600')

database_name = r'C:\Users\Alaud\OneDrive\Desktop\Python\SQLite\MyDatabase.db'      # write your location with database name

# database_name = r'/home/omar/git_workspace/code_for_Kids/classWork/alauddin/MyDatabase.db'

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
    placeholder is just a contained you created before inserting a value into it.
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

def delete():
    input_text = txt2.get('1.0','end')
    print(input_text)
    script =  'DELETE from book WHERE book_name = (?)'
    cur.execute(script, (input_text.strip(),)) 
    c.commit()  # saving
    cur.execute('SELECT * FROM book') 
    c.commit()
    print(cur.fetchall())

# text 1 where user will write the book name, author name and description
txt1 = Text(root, height=5, width=25, font='arial')
txt1.grid(row=0, column=0)

# button to insert data into the database
btn = Button(root, text='Add the Book', bd=5, command=add)
btn.grid(row=1, column=0)

txt2 = Text(root, height=5, width=25, font='arial')
txt2.grid(row=0, column=10)

btn = Button(root, text='Delete', bd=5, command=delete)
btn.grid(row=2, column=0)

root.mainloop()