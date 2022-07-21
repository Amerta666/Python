# 2. Задайте список. Напишите программу, которая определит,
#    присутствует ли в заданном списке строк некое число.


# def SearchList(arr, number):
#     for i in arr:
#         if i == str(number):
#             return 'yes'
#     return 'no'
#
# list1 = ['gdfgahadfhas', 'fgadgfda', 'fadgfadg', '56']
#
# print(SearchList(list1, 56))
# ---------------------------------------------------------
def searchList(arr, number):
    if str(number) in arr:
        return 'yes'
    return 'no'


list1 = ['gdfgahadfhas', 'fgadgfda', 'fadgfadg', '56']
print(searchList(list1, 56))
# ---------------------------------------------------------

# list1 = ['gdfgahadfhas', 'fgadgfda', 'fadgfadg', '56']
# x = 56
# for i in list1:
#     if i == str(x):
#         print('yes')
#         exit()
# print('no')
