# given a sorted list implement binary search
# to find an element in the list

def binary_search(arr, element):
    left_index = 0
    right_index = len(arr) - 1
    while left_index <= right_index:
        middle = (left_index + right_index)//2
        if arr[middle] == element:
            return (middle, arr[middle])
        elif arr[middle] < element:
            left_index = middle + 1
        else:
            right_index = middle
    return -1



print(binary_search([1,2,3,4,5,6], 6))