a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = b**2 - 4*a*c

x1 = (-b + (delta**1/2)) / (2*a)

x2 = (-b - (delta**1/2)) / (2*a)

print('O delta é = ', delta)
print('O X1 é = ', x1)
print('O X2 é = ', x2)
