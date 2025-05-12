"""
given an array A = [1,4,9] add 1 and propagate it,
func(A) --> [1,5,0]
A = [9,9,9]
func(A) --> [1,0,0,0]
"""
# using python map function
def preci_increment(A):
    # convert elements of A to str and concatenate with join
    s = ''.join(map(str, A))
    # convert to integer and add 1, this will handle carrying digits
    s = int(s) + 1
    # use list comprehension to turn our answer back to an array of digits
    return [int(digit) for digit in str(s)]

print(preci_increment([1,9,9]))

def add_one(A):
    # add one to the last element
    A[-1] += 1
    # loop through the list and carry the one
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    # at the end, check if the first element is 10
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

print(add_one([1,9,9]))
