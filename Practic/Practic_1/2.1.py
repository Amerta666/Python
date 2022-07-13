# 2. Найти максимальное из пяти чисел

list = [1, 2, 12, 5, 8]
i = 0
max = list[i]
while i < len(list):
    if list[i] > max:
        max = list[i]
    i = i + 1
print(max)
