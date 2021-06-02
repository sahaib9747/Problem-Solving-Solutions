fib_cache = {}


def fibonacci(n):
    if n in  fib_cache:
        return fib_cache[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        value = fibonacci(n - 1) + fibonacci(n - 2) 
    fib_cache[n] = value
    return value


n = int(input())

for i in range(n):
    if i < n - 1:
        print("%i " % fibonacci(i) ,end="")
    else:
        print("%i" % fibonacci(i))