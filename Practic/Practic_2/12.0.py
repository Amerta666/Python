# 12. Сложить числа вещественного числа

a = input('Введите число: ')
sum = 0
for i in a:
    if (i.isdigit()):
        sum = int(i) + sum
print(sum)
