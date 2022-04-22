# 12. Сложить числа вещественного числа


a = input('Введите число: ')
sum = 0
for i in a:
    if (i.isdigit()):
        sum = int(i) + sum
print(sum)


# a = 424.7342
# while a % 1 != 0:
#     a = a * 10
# print(a)

# a = int(a)
# print(a)
# a = str(a)

# sum = 0

# for i in a:
#     i = int(i)
#     sum += i
# print(sum)