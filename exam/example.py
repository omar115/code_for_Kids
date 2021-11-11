print('----PYTHON SPLIT EXAMPLE-----\n\n')
# string split
text = 'Some#examples?of$the@force*of!gravity?include:The#force#that#holds#the#gases?in&the#sun.'

# split by #
ans = text.split('#')
print(ans)

# split by ?
ans = text.split('?')
print(ans)

# and others you can practice, i have given lots
# of things in the string, try it


print('\n\n----Python LOOP Example----\n\n')

# print 1 to 10 using while loop
i = 1
while(i <= 10):
    print(i)
    i = i + 1


# print only even number between 1 to 10 using while loop or for loop
i = 1
while(i <= 10):
    if i % 2 == 0:
        print(i)
    i = i + 1