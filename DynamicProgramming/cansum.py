# write a function cansum(targetsum,numbers) that takes in a targetsum and an array of numbers as arguments
# the returns True or False indicating whether or not it is possible to generate the
# targetsum using the numbers from the array.

def cansum(target,numarr,memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for element in numarr:
        remainder = target - element
        if cansum(remainder, numarr, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False
    

print(cansum(7,[2,4])) #False
print(cansum(15,[1,2,3,5])) #True
print(cansum(8,[1,2,3,5])) #True
print(cansum(6,[1,2,3,5])) #True
print(cansum(7,[1,2,3,5])) #True
print(cansum(300,[7,14])) # False