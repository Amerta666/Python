# 2. Найти максимальное из пяти чисел

# list = [2, 2, 8, 20, 5]
# max = list [0]
# if list [1] > max:
#     max = list[1]
# if list[2] > max:
#     max = list[2]
# if list[3] > max:
#     max = list[3]
# if list[4] > max:
#     max = list[4]
# print(max)

# list = [1, 2, 12, 5, 8]
# i = 0
# max = list[i]
# while i<len(list):
#     if list[i] > max:
#         max=list[i]
#     i=i+1
# print(max)

numbers = [4, 10, 15, 8, 20]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)