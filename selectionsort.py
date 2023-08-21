def selectionsort(arr):
    for i in range(len(arr) -1):
        minimum_index = i
        for j in range(i+1,len(arr)):
            if arr[minimum_index] > arr[j]:
                minimum_index = j
        if minimum_index != i:
            arr[i],arr[minimum_index] = arr[minimum_index], arr[i]
    return arr


a = [3,8,5,1,10]
b = [1,2,3,4,5,6]
c = []
d = [6,5,4,3,2,1]

print(selectionsort(a))
print(selectionsort(b))
print(selectionsort(c))
print(selectionsort(d))