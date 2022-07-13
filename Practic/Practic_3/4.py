# 4. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

list = []
n = int(input('Введите число N: '))
summ = 0
a = 0
for i in range(1, n + 1):
    a = (1 + 1/i)**i
    list.append(a)
print(list)

for i in list:
    summ += i
print(summ)