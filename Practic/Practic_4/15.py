# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

s = '645 5649 2345 645 232 6545 4786'

s2 =[]
for i in s.split():
    s2.append(int(i))
print(s2)

print(max(s2), min(s2))