# write a function that takes in a a targetsum and an array of numbers as arguments
#Then returns an array containing any combination of elements that add up to exactly the targetsum
# return null if no combination of elements
# if there are multiple combinations you can return any single one
# example howsum(7,[2,3,5,7]) --> [7] or [2,5] or [2,2,3]
def howsum(target,numarr,memo=None):
    # memoized 
    #time: O(n*m^2)
    #space: O(m^2)
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for element in numarr:
        remainder = target-element
        result = howsum(remainder,numarr,memo)
        if result is not None:
            memo[target] = result + [element]
            return memo[target]
    memo[target] = None
    return None
# def howsum(target,numarr):
#     # Brute force solution
#     # time: O(n^m * m)
#     # space: O(m)
#     if target == 0:
#         return []
#     if target < 0:
#         return None
#     for element in numarr:
#         remainder = target-element
#         result = howsum(remainder,numarr)
#         if result is not None:
#             return result + [element]
#     return None
    

print(howsum(7,[2,4])) #False
print(howsum(15,[2,3,5])) #True
print(howsum(8,[2,3,5])) #True
print(howsum(6,[2,3,5])) #True
print(howsum(7,[2,3,5])) #True
print(howsum(300,[7,14])) # False