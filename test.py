def add(x,y):
    x = 10
    y = 12
    z=2
    print(z)
    return x, y

global z
x=1
y=2

x, y = add(x,y)

print(x)
print(y)
