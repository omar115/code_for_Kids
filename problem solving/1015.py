import math

a = input().split(' ')
b = input().split(' ')

x1 = float(a[0])
y1 = float(a[1])
x2 = float(b[0])
y2 = float(b[1])

result = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print('{:.4f}'.format(result))