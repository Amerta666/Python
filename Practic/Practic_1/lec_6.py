# 6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

days_of_the_week = ['Monday', 'Tuesday','Wednesday','Thursday','Friday', 'Saturday', 'Sunday']

day = int(input('Введите день недели: '))

if day > 5:
    print('Выходной')

print(days_of_the_week[day - 1])
