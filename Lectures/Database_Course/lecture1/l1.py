import sqlite3

path = '/home/akash/git_workspace/code_for_Kids/Lectures/Database_Course/lecture1/'

conn = sqlite3.connect(path+'customer.db')

# create a cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    
    )""")

# notes: data types in sqlite3
# NULL: Means you can keep the field empty
# Integer: 1,2,3,..
# Real: Decimal Values
# Text: String
# Blob: can keep anything (images, videos, etc.)

conn.commit()

conn.close()