# 5. Напишите программу, которая принимает на вход число и проверяет,
#     кратно ли оно 5 и 10 или 15, но не 30.

a = int(input("Введите число: "))
if a % 30 == 0:
    print("Число кратно 30")
    exit()
if a % 5 == 0 and a % 10 == 0:
    print("Число кратно 5 и 10")
elif a % 15 == 0:
    print("Число кратно 15")
else:
    print("Число не кратно 5 и 10 или 15")
# -------------------------------------------------
# a = int(input("Введите число: "))
#
# if a % 5 == 0 and a % 10 == 0 and a % 30 != 0 or a % 15 == 0 and a % 30 != 0:
#     print("Число кратно 5 и 10 или 15, но не 30")
# else:
#     print("Число кратно 30")