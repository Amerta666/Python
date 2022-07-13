# 16. Найти корни квадратного уравнения Ax² + Bx + C = 0

a = float(input('Введите A: '))
b = float(input('Введите B: '))
c = float(input('Введите C: '))

d = (b**2 - 4 * a * c)

print('Дискриминант равен = ', d)

if d > 0:
    x1 = ((-b - (d**0.5)) / (2*a))
    x2 = ((-b + (d**0.5)) / (2*a))
    print('X1 =',(round(x1, 4)))
    print('X2 =',(round(x2, 4)))
elif d == 0:
    x = (- b / (2 * a))
    print('X =', x)
else:
    print('Решений не существует')
