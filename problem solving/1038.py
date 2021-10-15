a = input().split(' ')
x = int(a[0])   # code
y = int(a[1])   # quantity

if x == 1:
    rst = y * 4.00
    print('Total: R$ {:.2f}'.format(rst))

elif x == 2:
    rst = y * 4.50
    print('Total: R$ {:.2f}'.format(rst))

elif x == 3:
    rst = y * 5.00
    print('Total: R$ {:.2f}'.format(rst))

elif x == 4:
    rst = y * 2.00
    print('Total: R$ {:.2f}'.format(rst))

elif x == 5:
    rst = y * 1.50
    print('Total: R$ {:.2f}'.format(rst))

