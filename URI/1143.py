def recursion(n, i=1):
    print("%i %i %i" % (i, i ** 2, i * i ** 2))
    if i == n:
        return 0
    i += 1
    recursion(n, i)


recursion(int(input()))