# 16. Написать программу проверки, является ли строка палиндромом

string = 'qwertytrewq'

len_rez = 1
j = 1
rez = False
for i in string:
    if j <= len(string) // 2:
        if i == string[len(string) - len_rez]:
            len_rez += 1
            j += 1
            rez = True
        else:
            print('Строка не является палиндромом')
            rez = False
            break
if rez == True:
    print('Строка является палиндромом')