import math
a = input().split(" ")
b = input().split(" ")

x1 = int(a[0])
y1 = int(a[1])

x2 = int(b[0])
y2 = int(b[1])

p1 = (x2-x1)**2
p2 = (y2-y1)**2
p3 = (p1)+(p2)

# Solving the equation using sqrt
res = math.sqrt(p3)
print("{:.4f}".format(res))