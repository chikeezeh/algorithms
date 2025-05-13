"""
Given two sorted arrays, find the unique intersection of the two arrays
Example:
A = [2,3,3,5,7,11]
B = [3,3,7,15,31]
result = [3,7]

"""
def intersect_sorted_array(A,B):
    # create two pointers
    a_pointer = 0
    b_pointer = 0
    intersection = []
    while a_pointer < len(A) and b_pointer < len(B):
        if A[a_pointer] == B[b_pointer]:
            if a_pointer == 0 or A[a_pointer] != A[a_pointer -1]:
                intersection.append(A[a_pointer])
            a_pointer += 1
            b_pointer += 1
        elif A[a_pointer] < B[b_pointer]:
            a_pointer +=1
        else:
            b_pointer += 1
    return intersection

A = [3,3,3,5,7,11]
# A = [3,3,3,3,3]
# B = [3,3,7,15,31]
B = [3,3,3,3,3,7]
print(intersect_sorted_array(A,B))
