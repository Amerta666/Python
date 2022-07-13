# 6. Реализовать алгоритм перемешивания списка.

import datetime
from time import time


rand_range = b - a
time.sleep(0.001)
ns = datetime.datetime.now().microsecond
for i in range(2):
    ns **= 2
    ns //= 100000
    ns %= 100000
return ns % rand_range + a

def my_shuffle(init_list):
    for i in range(len(init_list)):
        index = my_random(0, len(init_list))
        (init_list[i], init_list[index]) = (init_list[index], init_list[i])
    return init_list

initial_list = '22. Реализовать алгоритм перемещения списка.'.split()
print(initial_list)
print(my_shuffle(initial_list))