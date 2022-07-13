# 12. В заданном списке вещественных чисел найдите разницу между максимальным и 
#     минимальным значением дробной части элементов. 
#     Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5.02, 10.01]
list1 = []
for i in list:
    list1.append(round(i - int(i), 2))
print(list1)

max = list1[0]
min = list1[0]

for i in list1:
    if i > max:
        max = i
    if i < min:
        min = i

print(round(max - min, 2))

