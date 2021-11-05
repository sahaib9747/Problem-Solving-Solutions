import sys

cache = {}

def fibo(n):
    if n in cache:
        return cache[n]
    
    if n == 0:
        val = 0
    if n == 1:
        val = 1
    if n >= 2:
        val = fibo(n-1) + fibo(n-2)
    
    cache[n] = val 

    return val

num = int(input())
for i in range(num):
    print('fibo', fibo(i))