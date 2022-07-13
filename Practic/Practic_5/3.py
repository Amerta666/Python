# 3. Даны два файла в каждом из которых находится запись многочлена. 
#    Сформировать файл содержащий сумму многочленов.
#  - Прочитать, вытянуть в список, потом строчки разделить
from os import remove
from posixpath import split


data1 = open('Practic/Practic_5/Practice_5_3_1.txt','r') # '3*x^6 + 3*x^4 + 8*x^3 + 9*x^2 + 4*x1 + 10 = 0'
data2 = open('Practic/Practic_5/Practice_5_3_2.txt','r') # '10*x^6 + 7*x^5 + 3*x^4 + 1*x^3 + 1*x^2 + 3*x^1 = 0'

list1 = []
list2 = []

for i in data1:
    list1.append(i)
for i in data2:
    list2.append(i)

list1 = list1[0].split(' ')
list2 = list2[0].split(' ')

list1 = [i for i in list1 if i not in {'+', '=', '0'}]
list2 = [i for i in list2 if i not in {'+', '=', '0'}]
print(list1)
print(list2)

list1_1 = []
list1_2 = []

print(list1)