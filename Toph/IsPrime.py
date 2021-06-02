from math import sqrt, ceil


def isPrime(n):
    result = True
    if n <= 1:
        result = False
    elif n > 2:
        if n % 2 == 0:
            result = False
        else:
            for i in range(3, int(ceil(sqrt(n))) + 1):
                if n % i == 0:
                    result = False
                    break
    return result


num = int(input())
if isPrime(num):
    print("Yes")
else:
    print("No")
