def fib_num(n):
    if n in (1, 2):
        return n
    else:
        return fib_num(n-1) + fib_num(n-2)


print(fib_num(10))