# 6. Напишите программу, удаляющую из текста все слова содержащие "абв".

string = 'абв щщш лщипи опоабвшщ шптш оабв'

string1 = (' '.join(i for i in string.split(' ') if 'абв' not in i))

print(string)
print(string1)
#print(' '.join(i for i in string.split(' ') if 'абв' not in i))