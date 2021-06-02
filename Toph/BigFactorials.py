def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

fac = int(input())

stringFac = str(factorial(fac))
if len(stringFac) < 3:
    print(stringFac)
else:
    print(stringFac[-4: ])