# 7. Напишите программу для. проверки истинности утверждения
#    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input('Введите X: '))
y = bool(input('Введите Y: '))
z = bool(input('Введите Z: '))

print(-(x or y or z) == (-x and -y and -z))