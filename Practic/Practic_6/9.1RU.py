
st = '1+2-3*4*5'
list = []

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

def operate(list, operator):
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
                if operator == '*':
                    sum = a * b
                elif operator == '/':
                    sum = a / b
                elif operator == '-':
                    sum = a - b
                elif operator == '+':
                    sum = a + b
                list[i - 1] = sum
                list.pop(i + 1)
                list.pop(i)
                size = len(list)
    return list


print(list)
list = operate(list, '*')
list = operate(list, '/')
list = operate(list, '+')
list = operate(list, '-')
print(list[0])
