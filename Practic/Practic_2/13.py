# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой

# a = input('Введите символы: ')
# b = input('Введите символы: ')
# a_list = str(a)
# b_list = str(b)
# j = 0
# count = 0
# for i in a:
#     for j in b:
#         if i == j:
#             count = count + 1
# print(count)

a = 'Привет'
b = 'Привет Мир! Привет Друг! Привет Залуп!'

count = 0

print(b.split(' '))

for i in b.split(' '):
    if i == a:
        count+=1
print(count)


# for i in range(len(b.split(' ')):
#     if a == b.split(' ')[i]:
#         count+=1
# print(count)
