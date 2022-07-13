f = open('mn.txt', 'r')
list1 = []
for i in f:
    # print(i)
    if i != '\n':
        list1.append(i)
 
# print(list1)
 
list2 = list1[0].split(' ')
# print(list2)
list3 = list1[1].split(' ')
# print(list3)
 
list2 = [i for i in list2 if i not in {'+', '0\n', '='}]
print(list2)
 
list2_2 = []
for i in list2:
    # print(i[-1])
    # exit()
    if len(i) <= 2:
        list2_2.append(i)
    elif i[-1] == '6':
        if i[1] == '*':
            list2_2.append(i[0])
        elif i[2] == '*':
            list2_2.append(i[:2])
    elif i[-1] == '5':
        if i[1] == '*':
            list2_2.append(i[0])
        elif i[2] == '*':
            list2_2.append(i[:2])
    elif i[-1] == '4':
        if i[1] == '*':
            list2_2.append(i[0])
        elif i[2] == '*':
            list2_2.append(i[:2])
    elif i[-1] == '3':
        if i[1] == '*':
            list2_2.append(i[0])
        elif i[2] == '*':
            list2_2.append(i[:2])
    elif i[-1] == '2':
        if i[1] == '*':
            list2_2.append(i[0])
        elif i[2] == '*':
            list2_2.append(i[:2])
    elif i[-1] == '1':
        if i[1] == '*':
            list2_2.append(i[0])
        elif i[2] == '*':
            list2_2.append(i[:2])
    else:
        list2_2.append(0)
 
print(list2_2)
 
list3 = [i for i in list3 if i not in {'+', '0\n', '='}]
print(list3)
 
list3_3 = []
for i in list3:
    if len(i) <= 2:
        list3_3.append(i)
    elif i[1] == '*':
        list3_3.append(i[0])
    elif i[2] == '*':
        list3_3.append(i[:2])
 
print(list3_3)