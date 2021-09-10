a = input().split(" ")
val1 = int(a[0])
val2 = int(a[1])
val3 = float(a[2])

b = input().split(" ")

val4 = int(b[0])
val5 = int(b[1])
val6 = float(b[2])

result = (val2 * val3) + (val5 * val6)

print('VALOR A PAGAR: R$ {:.2f}'.format(result))


