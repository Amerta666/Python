# n = int(input("Введите число n: "))
# m = int(input("Введите число m: "))
# # print(int(n < m))
#
# if n % 2 == 0 and m % 2 == 0:
#     print("Оба числа чётные")
# elif n % 2 == 0:
#     print("Число n - чётное, m - нечётное")
# elif m % 2 == 0:
#     print("Число m - чётное, n - нечётное")
# else:
#     print("Оба числа нечётные")

# print(*range(5))

n = int(input("Введите число: "))
b = ''
while n > 0:
    b = str(n % 2) + b
    n //= 2
print(b)


