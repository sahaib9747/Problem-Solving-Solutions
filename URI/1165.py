import math
import sys


def prime(n, div, counter=3):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        if counter > div:
            return True
        elif n % counter == 0:
            return False
    counter += 2
    return prime(n, div, counter)


def main():
    half = lambda x: int(math.sqrt(x))
    msg = ["nao eh primo", "eh primo"]
    with sys.stdin as file:
        tCase = file.readline().strip()
        display = [False] * int(tCase)
        for i in range(int(tCase)):
            case = file.readline().strip()
            result = prime(int(case), half(int(case)))
            display[i] = "%s %s" % (case, msg[result])
    print(*display, sep='\n')

    
if __name__ == '__main__':
    main()