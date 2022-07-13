# 8. Определить, присутствует ли в заданном списке строк, некоторое число.

list = ['a, 2, 4', 
        't, 6, 2', 
        'f, 1, 3']

n = input('Введите искомое число: ')

answer = False
for i in range(len(list)):
    for j in list[i]:
        if j == n:
            answer = True

if answer == False:
    print('Не присутствует')
else:
    print('Присутствует')