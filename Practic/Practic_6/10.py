# 10. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
#    входные и выходные данные хранятся в отдельных текстовых файлах

data = 'aaaabbcdddaa'
start = ''
final = ''
count = 1
for i in data:
    if i != start:
        if start != '':
            final += str(count) + start
        count = 1
        start = i
    else:
        count += 1
final += str(count) + data[-1]
print(final)
