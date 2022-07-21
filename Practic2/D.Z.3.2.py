# 3.2. Напишите программу, которая найдёт произведение пар чисел списка.
#      Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#      Пример:
#      - [2, 3, 4, 5, 6] => [12, 15, 16];
#      - [2, 3, 5, 6] => [12, 15]

def pairsOfNum(arr):
    last = len(arr)
    list2 = []
    i = 0
    while last // 2 >= i:
        list2.append(arr[i] * arr[last - 1])
        i += 1
        last -= 1
    if len(arr) % 2 != 0:
        list2.append(list1[len(arr) // 2] ** 2)
    return list2


list1 = [2, 3, 4, 5, 6]
print(pairsOfNum(list1))
