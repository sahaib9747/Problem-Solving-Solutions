from math import ceil, sqrt 

def is_prime(n):
    if n <= 1:
        return False
    if n > 2:
        if n % 2 == 0:
            return False 
        else:
            limit = ceil(sqrt(n))
            for i in range(3, limit+1):
                if n % i == 0:
                    return False
    return True


def check(asciis):
    for i in asciis:
        if is_prime(i):
            print('YES')
            break
    else:
        print('NO')


def main():
    inp = int(input())

    for i in range(inp):
        lst = input().split()
        lst[1] = int(lst[1]) 

        values = [ord(i) + lst[1] for i in lst[0]]   

        check(values)

main()
