import sqlite3

# where you want to save the database
# database location
database_name = '/home/akash/git_workspace/code_for_Kids/classWork/my_database.db'
# name = 'customer.db'    # .db is the extention of database

c = sqlite3.connect(database_name)




cur = c.cursor()    # similar to pygame, it has many buit in methods/functions

# sTEP 1: cREATE A tABLE

cur.execute("INSERT INTO customers VALUES ('Bill',NULL,'bill@gmail.com')")


# Sqlite3 data types
# NULL: you can keep it empty
# Integer: 1,2,3
# Real: decimal values 1.22
# Text: String
# Blob: you can keep anything like images, videos, audios, etc.

# saving the database
c.commit()

# closing the database
c.close()