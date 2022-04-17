# 4. Показать первую цифру дробной части числа

a = float(input('Введите число: '))
d = int(a * 10) % 10
print(d)


# Вариант через стринг
# a = 12.322
# b = str(a)
# for i in range(len(b)):
#     if b[i] == '.':
#         print(b[i+1])
