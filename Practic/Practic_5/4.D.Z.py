# 4. В файле находится N натуральных чисел, записанных через пробел.
#   Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
#   Пример: 2, 3, 4, 6, 7 (не хватает 5, её и добавить в нужное место) insert в помощь

def repair(list):
    list = list[0].split(', ')
    list = [int(i) for i in list]
    size = len(list)
    i = 1
    for i in list:
        if i >= size:
            break
        if (list[i] - 1 != list[i - 1]):
            list.append(list[i] - 1)
            list = sorted(list)
            size = len(list)
            i = 1
        i+=1
    return list

data = open('Practic/Practic_5/DZ.4.txt', 'r')

list = []
for i in data:
    list.append(i)
data.close  
print(list)            #  ['2, 3, 4, 6, 7, 9, 11']
print(repair(list))    #  [2, 3, 4, 5, 6, 7, 8, 9, 11]