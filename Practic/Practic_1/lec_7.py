# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = bool(input('Введите X: '))
y = bool(input('Введите Y: '))
z = bool(input('Введите Z: '))

def function (X,Y,Z):
    if -(x or y or z) == (-x and -y and -z):
        return True
    else:
        return False

print(function(x,y,z))