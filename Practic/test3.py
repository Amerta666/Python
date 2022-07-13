list = [13,12,11,10,9,8,7,6,5,4,3,2,1] 
 
list1 = [] 
for i in list: 
    list1.append(i) 
 
 
for i in range(len(list1) - 1): 
    for j in range(len(list1) - 1 - i): 
        if list1[j] > list1[j+1]: 
            list1[j], list1[j+1] = list1[j+1], list1[j] 
            j += 1 
 
 
print(list) 
print(list1)


