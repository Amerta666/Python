# 2. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#    (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#    *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# при k = 4, 99x^4 + 78x^3 + 8x^2 + 78x + 89 = 0

from fileinput import close
from ntpath import join
from random import randint

k = int(input('Введите k:'))
list = [randint(0, 10) for i in range(k + 1)]
print(list)
res = [f'{list[i]}*x^{len(list)-i-1}' if len(list)-i-1 != 0 else f'{list[i]}' for i in range(len(list)) if list[i] !=0]
print(res)
print(' + '.join(res) + ' = 0')

data = open('Practic/Practic_5/Practice_5_2.txt', 'a') 
data.write(' + '.join(res) + ' = 0 \n')
data.close
