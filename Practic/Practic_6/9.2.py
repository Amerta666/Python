# 9. Написать программу вычисления арифметического выражения заданного строкой.
#   Используются операции +,-,/,*. приоритет операций стандартный.
#   Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
#   Добавить возможность использования скобок, меняющих приоритет операций.
#   Пример: 1+2*3 => 7; (1+2)*3 => 9;

st = '1+2-3*4/5'
list = []
sum = None


def multi(list):
    for i in range(size):
        if i >= size:
            break
        if list[i] == '*':
            sum = list[i-1] * list[i+1]
            list[i - 1] = sum
            list.pop(i + 1)
            list.pop(i)
            size = len(list)
    return list

def div (list):
    for i in range(size):
        if i >= size:
            break
        if list[i] == '/':
            sum = list[i-1] / list[i+1]
            list[i - 1] = sum
            list.pop(i + 1)
            list.pop(i)
            size = len(list)
    return list

def subtr (list):
    for i in range(size):
        if i >= size:
            break
        if list[i] == '-':
            sum = list[i-1] - list[i+1]
            list[i - 1] = sum
            list.pop(i + 1)
            list.pop(i)
            size = len(list)
    return list

def addition (list):
    for i in range(size):
        if i >= size:
            break
        if list[i] == '+':
            sum = list[i-1] + list[i+1]
            list[i - 1] = sum
            list.pop(i + 1)
            list.pop(i)
            size = len(list)
    return list

for i in st:
    if i.isdigit() == True:
        list.append(int(i))
    elif i == '+':
        list.append('+')
    elif i == '-':
        list.append('-')
    elif i == '*':
        list.append('*')
    elif i == '/':
        list.append('/')

print(list)
size = len(list)

list = multi(list)
list = div(list)
list = subtr(list)
list = addition(list)
print(list)