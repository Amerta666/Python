
def Sort(source, first, last):
    left = first
    right = last
    middle = source[(first + last / 2)]
    condition = True
    do = True
    while do:
        left <= right
        while (source[left] < middle):
            left += left
        while (source[right] > middle):
            right -= right
        if (left <= right):
            if(source[left]>source[right]):
                temp = source[left]
                source[left] = source[right]
                source[right] = temp
        left += 1
        right -= 1
    do = condition
    if (left < last):
        Sort(source, left, last)
    if (first < right):
        Sort(source, first, right)


list = [1, 5, 4, 2, 6, 7, 8]
print(list)
Sort(list, 0, (len(list)-1))
print(list)
