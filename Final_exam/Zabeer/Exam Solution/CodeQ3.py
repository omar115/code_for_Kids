a = int(input("Give numbers even or odd: "))
b = int(input("Give numbers even or odd: "))
c = int(input("Give numbers even or odd: "))
d = int(input("Give numbers even or odd: "))
e = int(input("Give numbers even or odd: "))


count = 0


if a % 2 == 0:
    print("even")
    count = count + 1
else:
    print("not even")

if b % 2 == 0:
    print("even")
    count = count + 1
else:
    print("not even")

if c % 2 == 0:
    print("even")
    count = count + 1
else:
    print("not even")

if d % 2 == 0:
    print("even")
    count = count + 1
else:
    print("not even")

if e % 2 == 0:
    print("even")
    count = count + 1
else:
    print("not even")

print(count)