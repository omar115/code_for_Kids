import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Connection to Sqlite3 DB successful')
    except Error as e:
        print(f"The error is '{e}' occured")



connect =  create_connection('/home/akash/git_workspace/code_for_Kids/Lectures/Database_Course/data.sqlite')
