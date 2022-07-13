# 14. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
#     Т.е. для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#     Негафибоначчи

k = 1

def nfib(n):
    if n in [1, 2]:
        return 1
    else:
        return nfib(n+2) - nfib(n+1)

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(0, k+1):
    list.append(nfib(-e))
list.reverse()

for e in range(1, k+1):
    list.append(fib(e))

print(list)  # [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
