# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#  - 6,78 -> 7
#  - 5    -> нет
#  - 0,34 -> 3

a = float(input("Введите число: "))
b = str(a)
for i in range(len(b)):
    if b[i] == ".":
        print(b[i + 1])
# ------------------------------------------
# a = input("Введите число: ")
# b = None
# for i in range(len(a)):
#     if (a[i] == ".") or (a[i] == ","):
#         b = int(a[i + 1])
#         print(b)
#         exit()
# else:
#     print(0)