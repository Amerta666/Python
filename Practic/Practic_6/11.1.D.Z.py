# 11. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#     Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

list = [1, 2, 3, 5, 1, 5, 3, 10]
list2 = []

repeat = False
for i in range(len(list)):
    repeat = False
    for j in range(len(list)):
        if i == j:
            continue
        if list[j] == list[i]:
            repeat = True
            break
    if not repeat:
        list2.append(list[i])

print(list2)
