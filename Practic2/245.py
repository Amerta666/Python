# 245. Будем называть числа круглыми, если они содержат в своей записи только цифры 0 и 5.
#      Составим последовательность неотрицательных целых круглых чисел в порядке возрастания:
#      0, 5, 50, 55, 500, 505 и так далее.
#      Написать программу, которая находит K-е по порядку в этой последовательности круглое число.
#      - 1 -> 0
#      - 2 -> 5
#      - 3 -> 50
#      - 4 -> 55
#      - 5 -> 500
#      - 6 -> 505
#      - 7 -> 550
#      - 8 -> 555
#      - 9 -> 5000

n = int(input("Введите число: "))
if n == 0 or n == 1:
    print(0)
    exit()
b = ''
n = n - 1
while n > 0:
    b = str(n % 2) + b
    n //= 2
c = int(b)
print(c*5)

