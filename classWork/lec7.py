'''
In this lecture, we will learn String Manipulation. We will learn how to apply
split function to slice a string and store in a variable.
'''

# String Manipulation

a = 'The Golden Fortress,Satyajit Ray,Detective'

# use split function to slice a string based on comma (,)
li = a.split(',')

print('The output after using split function is: \n',li)

# getting the value using index of a list

book_name = li[0]

author_name = li[1]

genre = li[2]

print('The book Name is:\n',book_name)
print('The Author Name is:\n',author_name)
print('The Book Genre is:\n',genre)

