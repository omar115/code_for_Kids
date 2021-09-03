from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter

root = Tk() 

root.geometry('1100x1000')

root.title('Library DB')

libdb = r'C:\Users\asuer\Documents\DbPython\libdb.db'  
# libdb = r'C:\Users\Ferntech\Desktop\git_workspace\code_for_Kids\classWork\leenat\libdb.db'

c = sqlite3.connect(libdb)     

cur = c.cursor()

try:
    cur.execute("""CREATE TABLE book (
        book_name text,
        author_name text,
        publication_date text,
        availability text
    )""")

except:
    print('database already created')

def add():
    input_text = txt1.get('1.0','end')
    
    output_text = input_text.split(',')     #slice the string given from text box 1
    
    # assign the output into different variables
    book_name = output_text[0]
    author_name = output_text[1]
    publication_date = output_text[2]
    availability = output_text[3]

    '''
    placeholder is just a container you created before inserting a value into it.
    it helps us during the operation of sqlite database. using question mark (?) you can create
    a placeholder into it.
    '''

    script = 'INSERT INTO book VALUES (?,?,?,?)' 
    cur.execute(script, (book_name, author_name, publication_date, availability))    
    c.commit() 
    cur.execute('SELECT * FROM book')  
    c.commit()  
    print(cur.fetchall())   


def delete():
    input_text = txt2.get('1.0','end')
    print(input_text)
    script =  'DELETE from book WHERE book_name = (?)'
    cur.execute(script, (input_text.strip(),)) 
    c.commit()  # saving
    cur.execute('SELECT * FROM book') 
    c.commit()
    print(cur.fetchall())   


def update():
    input_text = txt3.get('1.0','end')
    input_text = input_text.strip()
    print('------- ',input_text)
    output_text = input_text.split(',')    
    print(output_text)
    availability= output_text[0]
    book_name = output_text[1]
    script = 'UPDATE book SET availability = (?) where book_name = (?)' 
    cur.execute(script, (availability,book_name))     
    c.commit() 
    cur.execute('SELECT * FROM book')  
    print(cur.fetchall())   

def show_all():
    tree = ttk.Treeview(root, column=("column1","column2","column3","column4"), show="headings")
    tree.heading("#1",text="Book Name")
    tree.heading("#2",text="Author Name")
    tree.heading("#3",text="Publication Date")
    tree.heading("#4",text="Availability")
    tree.grid(row=0, column=5, pady=5)
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()

    for i in rows:
        tree.insert("",tkinter.END, values=i)

txt1 = Text(root, height=5, width=25, font='arial', bg = "floralwhite", fg = 'darkgrey')
txt1.grid(row=0, column=0, padx=10, pady=10)

btn1 = Button(root, text='Add the Book', bd=5, fg = "darkred", bg = "goldenrod", command=add)
btn1.grid(row=1, column=0, padx=10, pady=10)

txt2 = Text(root, height=5, width=25, font='arial', bg = "floralwhite", fg = 'darkgrey')
txt2.grid(row=2, column=0, padx=10, pady=10)

btn2 = Button(root, text='Delete the Book', bd=5, fg = "darkred", bg = "goldenrod", command=delete)
btn2.grid(row=3, column=0, padx=10, pady=10)

txt3 = Text(root, height=5, width=25, font='arial', bg = 'floralwhite', fg = 'darkgrey')
txt3.grid(row=4, column=0, padx=10, pady=10)

btn3 = Button(root, text='Update the Book', bd=5, fg = "darkred", bg = "goldenrod", command=update)
btn3.grid(row=5, column=0, padx=10, pady=10)

btn4 = Button(root, text='Show Book List', bd=5, fg = "darkred", bg = "goldenrod", command=show_all)
btn4.grid(row=6, column=0, padx=20, pady=20)


root.mainloop()