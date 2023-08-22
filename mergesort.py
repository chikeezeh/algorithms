def mergesort(arr):
    if len(arr) <=1:
        return arr
    # split the arr into two
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    # call merge_sort recursively
    mergesort(left_arr)
    mergesort(right_arr)

    # merge the sorted array
    i = 0 # left most element in left array
    j = 0 # left most element in right array
    k = 0 # index for arr
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    # if we have element left in the left array, we want to add each to the main array
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    # same for right array
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    return arr


a = [3,8,5,1,10]
b = [1,2,3,4,5,6]
c = []
d = [6,5,4,3,2,1]

print(mergesort(a))
print(mergesort(b))
print(mergesort(c))
print(mergesort(d))