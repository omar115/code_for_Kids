from tkinter import *
import sqlite3
import tkinter

root = Tk()

root.geometry('600x600')



# libdb = r'C:\Users\asuer\Documents\DbPython\libdb.db'
libdb = r'/home/omar/git_workspace/code_for_Kids/classWork/leenat/libdb.db'      

c = sqlite3.connect(libdb)

cur = c.cursor()

try:
    cur.execute("""CREATE TABLE book (
        book_name text,
        author_name text,
        genre text,
        publication_date text,
        number_of_pages text,
        availability text
    )""")

except:
    print('database already created')

def add():
    input_text = txt1.get('1.0','end')
    
    output_text = input_text.split(',')     
    book_name = output_text[0]
    author_name = output_text[1]
    genre = output_text[2]
    publication_date = output_text[3]
    number_of_pages = output_text[4]
    availability = output_text[5]
    '''
    placeholder is just a contained you created before inserting a value into it.
    it helps us during the operation of sqlite database. using question mark (?) you can create
    a placeholder into it.
    '''

    script = 'INSERT INTO book VALUES (?,?,?,?,?,?)' 

    cur.execute(script, (book_name, author_name, genre, publication_date, number_of_pages, availability))     

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
    # print(input_text)
    output_text = input_text.split(',')
    # print(output_text)
    a = output_text[0]
    b = output_text[1]
    script =  'UPDATE book SET availability = (?) WHERE book_name = (?)'
    cur.execute(script, (a, b)) 
    c.commit()  # saving
    cur.execute('SELECT * FROM book') 
    c.commit()
    print(cur.fetchall())

txt1 = Text(root, height=5, width=75, bg= 'Gainsboro')
txt1.grid(row=0, column=0)

btn = Button(root, text='Enter my book', bd=5, bg='lightsalmon', command=add)
btn.grid(row=1, column=0)

txt2 = Text(root, height=5, width=75, bg= 'Gainsboro')
txt2.grid(row=10, column=0)

btn1 = Button(root, text='Delete book entry', bd=5, bg='lightsalmon', command=delete)
btn1.grid(row=11, column=0)

txt3 = Text(root, height=5, width=75, bg= 'Gainsboro')
txt3.grid(row=20, column=0)

btn2 = Button(root, text='Update book entry', bd=5, bg='lightsalmon', command=update)
btn2.grid(padx=100, pady=0)

def printo(): 
    cur.execute("SELECT * FROM customers")
    print(cur.fetchall())

def show():
    tk.messagebox.showinfo('All Entries', printo())

button1 = Button(root, text='Show all book entries', bd=5, command=None,bg='Dark Slate Blue',fg='Dark Turquoise')
button1.grid(padx=50, pady=50)

root.configure(bg='Cornsilk')


root.mainloop()