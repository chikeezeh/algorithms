def bubblesort (arr):
    swap = True # allow us to enter the while loop for the 1st time.
    while swap:
        swap = False # if we have a sorted list, then we won't enter the second time.
        for i in range (len(arr) -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
    return arr

# naive solution
# def bubblesort (arr):
#     for j in range (len(arr)):
#         for i in range (len(arr) -1):
#             left = arr[i]
#             right = arr[i+1]
#             if left > right:
#                 arr[i] = right
#                 arr[i+1] = left
#     return arr

a = [3,8,5,1,10]
b = [1,2,3,4,5,6]
c = []
d = [6,5,4,3,2,1]
print(bubblesort(a))
print(bubblesort(b))
print(bubblesort(c))
print(bubblesort(d))