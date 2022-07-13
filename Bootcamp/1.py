
list = [1, 2, 10, 50, 2, 3, 6, 49, 54, 4]

list1 = []
for i in list:
    list1.append(i)

for i in range(len(list1) - 1):
    for j in range(len(list1) - 1):
        if list1[j] > list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
            j+=1

print(list)
print(list1)