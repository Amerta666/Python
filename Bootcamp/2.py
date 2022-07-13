import random as r

max = 5
data = [r.randint(0, max) for i in range(11)]
print(data)

counter = [0 for i in range(max+1)]
print(counter)

for item in data:
    counter[item] += 1
print(counter)

k = 0
for index in range(len(counter)):
    for i in range(counter[index]):
        data[k] = index
        k += 1
print(data)
