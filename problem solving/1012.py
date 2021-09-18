a = input().split(" ")

base1 = float(a[0])
base2 = float(a[1])
height = float(a[2])

triangle = 0.5 * base1 * height
circle = 3.14159 * height * height
trapezium = ( base1 + base2 ) / 2.0 * height
square = base2 * base2
rectangle = base1 * base2

print('TRIANGULO: {:.3f}'.format(triangle))
print('CIRCULO: {:.3f}'.format(circle))
print('TRAPEZIO: {:.3f}'.format(trapezium))
print('QUADRADO: {:.3f}'.format(square))
print('RETANGULO: {:.3f}'.format(rectangle))
