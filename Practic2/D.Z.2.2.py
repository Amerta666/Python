# 2.2 Напишите программу, которая принимает на вход число N и выдает
#     набор произведений чисел от 1 до N. Факториал
#     5! = 120

n = int(input('Введите число: '))
sum = 1
count = 1
for i in range(n):
      sum = sum * count
      print(sum, end=', ')
      count += 1