# 5. Задать список из N элементов, заполненных числами из [-N, N].
#    Найти произведение элементов на указанных позициях.
#    Позиции хранятся в файле file.txt в одной строке одно число

list = []
a = 1
n = int(input('Введите число N: '))
for i in range(-n, n+1):
    list.append(i)
print(list)

data = open('file.txt', 'r')

for i in data:
    index = int(i)
    a *= list[index]

data.close
print(a)