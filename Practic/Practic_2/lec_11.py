# 11. Напишите программу, которая выводит нечетные числа из заданного списка и
#     останавливается, если встречает число 554.

# r = range(0, 800)
# numbers = list(r)
# num = []
# for i in numbers:
#     if i == 554:
#         break
#     if (i % 2 == 1):
#         num.append(i)
# print(num)

r = range(200, 700)
numbers = list(r)
num = []
i = 0
while numbers[i] != 554:
    if numbers[i] % 2 != 0:
        num.append(numbers[i])
    i = i + 1
print(num)
