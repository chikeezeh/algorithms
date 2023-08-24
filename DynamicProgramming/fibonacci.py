def fib_rec(n):
    # naive solution
    if n <=2:
        return 1
    else:
        return (fib_rec(n-1) + fib_rec(n-2))

# def fib_rec(n):
#     # naive solution
#     if n <=2:
#         return 1
#     else:
#         return (fib_rec(n-1) + fib_rec(n-2))


print(fib_rec(1))
print(fib_rec(3))
print(fib_rec(5))
print(fib_rec(100))