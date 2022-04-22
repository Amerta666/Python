# 14. Посчитайте, сколько раз символ встречается в строке.

a = input('Введите строку: ')
b = input('Введите символ: ')

stroka = str(a)
count = 0
for i in stroka:
    if i == b:
        count += 1
print(count)