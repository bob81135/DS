def fib(n):
    if(n<2):
        return n
    else:
        a = 0
        b = 1
        for _ in range(2,n+1):
            c = a+b
            a = b
            b = c
        return c
print(fib(15))