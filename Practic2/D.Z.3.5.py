# * 3.5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#       *Пример:*
#       - для k = 8 список будет выглядеть так:
#       [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#       [Негафибоначчи]


def fib(k):
    if k < 0:
        return ("Введите число больше 0")
    if k == 0:
        return 0
    positive = [0, 1]
    negative = [0, 1]
    i = 2
    while i <= k:
        positive.append(positive[i - 1] + positive[i - 2])
        negative.append(negative[i - 2] - negative[i - 1])
        i += 1
    del(positive[0])
    negative.reverse()
    return negative+positive

k = int(input('Введите число: '))
print(fib(k))