# a = int(input())

# print(a*2 , 'minutos')


# 1042

a = int(input())
b = int(input())
c = int(input())

li = []

li.append(a)
li.append(b)
li.append(c)

li.sort()

print(li)

li2 = li

li2.sort(reverse=True)

print(li2)