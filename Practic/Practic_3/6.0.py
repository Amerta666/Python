# 6. Реализовать алгоритм перемешивания списка.

from random import randint


list1 = list(range(0, 21, 2))
list2 = []
index = 0

print(list1)

while len(list2) < len(list1):
    index = randint(0, len(list1)-1)
    if list1[index] not in list2:
        list2.append(list1[index])

print(list2)
