import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('The database is connected')
    except Error:
        print('The database is not connected')
        # print(e)

connect =  create_connection('/home/akash/git_workspace/code_for_Kids/Lectures/Database_Course/library_data')
