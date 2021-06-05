import sqlite3
import traceback

def create_database_connection(location):
    connection = None
    try:
        connection = sqlite3.connect(location)
        print('The database is connected')
    except:
        print('The database is not connected')
        print(traceback.format_exc())

location = r'/home/akash/git_workspace/code_for_Kids/data_base_first.py/data.sqlite'

create_database_connection(location)