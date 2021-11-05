import sys

def fac(n):
    if n == 0 or n == 1:
        return 1
    
    return n * fac(n-1)



num = int(input())

sys.setrecursionlimit(num+1000)

print(fac(num))

