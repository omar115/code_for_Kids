'''
here we will learn how to read a dataset using pandas library.
the dataset can be a simple xlsx or CSV format file.

How to install the Pandas library?
in your terminal type this command:

pip install pandas


'''
import pandas as pd

# read the database
data = pd.read_csv('tips.csv')

# print the database
# head function will display first 10 rows if 10 is given
# if you write 20 it will print first 20 rows
print(data.head(10))