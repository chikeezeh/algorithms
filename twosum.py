"""
Given an array A, and a target sum K, return two elements of A
where A[i] + A[j] == K
Example:
A = [2,3,4,5,7]
K = 11
Result = (4,7)
"""
def two_sum_brute(A, target):
    # loop through A twice and check if pairs add to target
    # O(n^2) time and O(1) space
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                return (A[i], A[j])
    return "No pair"
def two_sum_hash(A, target):
    # this uses a hashmap to store the elements as we 
    # traverse the array
    # O(n) time and 0(n) space
    target_hash = {}
    for element in A:
        if element in target_hash:
            return (target_hash[element], element)
        else:
            target_hash[target - element] = element
    return "No pair"


print(two_sum_brute([2,3,4,5,7], 11))
print(two_sum_hash([2,3,4,5,7], 11))