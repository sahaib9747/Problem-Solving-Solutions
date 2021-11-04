from math import ceil, sqrt 

def is_prime(n):
    if n <= 1:
        return False
    if n > 2:
        if n % 2 == 0:
            return False 
        else:
            limit = ceil(sqrt(n))
            print(limit)
            for i in range(3, limit+1):
                if n % i == 0:
                    return False
    return True


i = int(input())
if is_prime(i):
    print(True)
else:
    print(False)