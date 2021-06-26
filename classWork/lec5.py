import sqlite3

# where you want to save the database
# database location
database_name = '/home/akash/git_workspace/code_for_Kids/classWork/my_database.db'
# name = 'customer.db'    # .db is the extention of database

c = sqlite3.connect(database_name)

cur = c.cursor()    # similar to pygame, it has many buit in methods/functions

# CREATE == INSERT
# RETRIEVE == FETCHALL
# UPDATE == UPDATE
# DELETE == DELETE

# update the value of database

cur.execute(" DELETE from customers WHERE email='LA@gmail.com' ")

c.commit()

cur.execute("SELECT * FROM customers")

print(cur.fetchall())

# saving the database
c.commit()

# closing the database
c.close()