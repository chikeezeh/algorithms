# base case grid_traveler (1,1) --> 1
# base case 2 grid_traveler(m,0) or (0,n) ---> 0
def grid_traveler(m,n, memo={}):
    # with memoization and using commutative property, where f(m,n) = f(n,m)
    if (m,n) in memo or (n,m) in memo:
        return memo[(m,n)]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    else:
        memo[(m,n)] = (grid_traveler(m-1,n,memo) + grid_traveler(m, n-1,memo))
        memo[(n,m)] = memo[(m,n)]
        return memo[(m,n)]

# def grid_traveler(m,n):
#     # naive
#     if m == 1 and n == 1:
#         return 1
#     if m == 0 or n == 0:
#         return 0
#     else:
        return (grid_traveler(m-1,n) + grid_traveler(m, n-1))

print(grid_traveler(2,3))
print(grid_traveler(0,3))
print(grid_traveler(4,3))
print(grid_traveler(3,4))
print(grid_traveler(10,3))
print(grid_traveler(18,18))