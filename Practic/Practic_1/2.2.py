# 2. Найти максимальное из пяти чисел

numbers = [4, 10, 15, 8, 20]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)
