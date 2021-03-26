def greet_user():
    print("hello, hope your are doing fine. stay safe at your home")

greet_user()

#pass information to function
def greet_user(username):
    print("hello, hope your are doing fine. stay safe at your home",username)

greet_user('raheel')

#more arguements to function

def greet_user(username,username2):
    print("hello, hope your are doing fine. stay safe at your home",username)
    print("By the way how is :",username2)
greet_user('raheel','anoy')
