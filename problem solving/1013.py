import math

x = input().split(" ")

a = int(x[0])
b = int(x[1])
c = int(x[2])

result = ( a + b + abs(a - b) ) / 2 

result2 =  int(( result + c + abs(result - c) ) / 2)

print(result2, 'eh o maior')
