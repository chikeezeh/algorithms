def insertionsort(arr):
    if len(arr) <=1:
        return arr
    for i in range(1,len(arr)):
        value_to_sort = arr[i]
        while value_to_sort < arr[i-1] and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    return arr


a = [3,8,5,1,10]
b = [1,2,3,4,5,6]
c = []
d = [6,5,4,3,2,1]

print(insertionsort(a))
print(insertionsort(b))
print(insertionsort(c))
print(insertionsort(d))