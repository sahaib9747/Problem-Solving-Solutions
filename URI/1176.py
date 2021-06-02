import sys

value = {}


def fibo(n):
    if n in value:
        return value[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n >= 2:
        result = fibo(n - 1) + fibo(n - 2)
        value[n] = result
    return result


with sys.stdin as file:
    tCase = file.readline().strip()
    display = []
    for i in range(int(tCase)):
        case = file.readline().strip()
        display.append("Fib(%s) = %i" % (case, fibo(int(case))))
    print(*display, sep='\n')
