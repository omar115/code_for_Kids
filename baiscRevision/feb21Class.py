#revision
"""
1. Basic Data Type
2. addition, 
3. if else, nested if else
4. for loop, while loop, (loop + if else)
5. function

"""

var1 = 100 #integer
var2 = 100.501 #float
var3 = True     #boolean
var4 = 'Python' #string

#how to check the type of these variables?
# print(type(var1))
# print(type(var3))

#how to print something
# print('Hello World!')   #single string print
# + == generic addition
# , == generic addition with type change
# print(var2 + var4)  # var2 + var4
# print(var2 , var4)  # var2 = str(var2) + 'Python'

#string Manipulation::: addition

# result = "float value: "+ str(var2) +" "+"string value: "+ var4 +" "+"boolean: "+ str(var3)

# print(result)

#if else for boolean types
'''
var5 = False     #take an umbrella or not
rainy_weather = False

if rainy_weather == True:
    if var5 == True:
        print('You just save yourself from rain')
    elif var5 == False:
        print('you will get drenched in rain')

elif rainy_weather == False:
    if var5 == True:
        print('smart boy')

    else:
        print('lucky!!')

else:
    print('You are not saved')
'''

# for i in range(5):

#     print(i)
#     if i == 2:
        
#         print('Black Widow')
    
#     if i % 2 == 0:
#         print('BATMAN')
    
#     else:
#         print('Spiderman')

# i = 1
# while i < 5:
#     print(i)
#     i = i + 1

#function

def addition():
    a = 5
    b = 5
    print('The addition function output is ')
    print(a+b)

# addition()

#parameter or argument pass

def substraction(value):
    a = 10
    print('The substraction value is ')
    print(a - value)

substraction(3)
