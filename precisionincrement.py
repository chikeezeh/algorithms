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

print(preci_increment([9,9,9]))

