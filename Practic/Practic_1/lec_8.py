# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

x = int(input('Введите X: '))
y = int(input('Введите Y: '))

if (x > 0 and y > 0):
    print('Точка находится в I четверти')
elif (x < 0 and y > 0):
    print('Точка находится во II четверти')
elif (x < 0 and y < 0):
    print('Точка находится в III четверти')
elif (x > 0 and y < 0):
    print('Точка находится в IV четверти')
else:
    print('Точка с координатами "0" : "0"')