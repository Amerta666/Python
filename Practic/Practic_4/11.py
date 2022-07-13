# 11. Найти произведение пар чисел в списке.
#     Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
#      list[len(list) - 1])

list = [2, 3, 4, 5, 6]
list2 = []
size = 1
for i in range((len(list) + 1) // 2):
    list2.append(list[i] * list[len(list) - size - i])
    print(list[len(list) - size - i])
    print(list[i])

print(list2)