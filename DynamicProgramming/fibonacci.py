def fib_rec(n, memo={}):
    # optimized solution
    if n in memo:
        return memo[n]
    if n <=2:
        return 1
    else:
        memo[n] = (fib_rec(n-1, memo) + fib_rec(n-2, memo))
        return memo[n]

# def fib_rec(n):
#     # naive solution
#     if n <=2:
#         return 1
#     else:
#         return (fib_rec(n-1) + fib_rec(n-2))


print(fib_rec(1))
print(fib_rec(2))
print(fib_rec(3))
print(fib_rec(4))
print(fib_rec(5))
print(fib_rec(6))
print(fib_rec(7))
print(fib_rec(50))