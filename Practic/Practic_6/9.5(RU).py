
st = '1+21-3*4*5'
list = []
current_number = ''

for i in st:
    if i.isdigit() == True:
        current_number += i
    else:
        list.append(int(current_number))
        current_number = ''
        if i == '+':
            list.append('+')
        elif i == '-':
            list.append('-')
        elif i == '*':
            list.append('*')
        elif i == '/':
            list.append('/')
if len(current_number) > 0:
    list.append(int(current_number))

def operate(list, operator, fn):
    print(list)
    size = len(list)
    sum = None
    for i in range(size):
        for j in range(size):
            if i >= size:
                break
            if list[i] == operator:
                a = list[i-1]
                b = list[i+1]
                sum = fn(a, b)
                list[i - 1] = sum
                list.pop(i + 1)
                list.pop(i)
                size = len(list)
    return list


print(list)
list = operate(list, '*', lambda a, b: a * b)
list = operate(list, '/', lambda a, b: a / b)
list = operate(list, '+', lambda a, b: a + b)
list = operate(list, '-', lambda a, b: a - b)
print(list[0])
