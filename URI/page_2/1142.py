"""
value = [1, 2, 3]
for i in range(int(input())):
    print(*value, end=" ")
    print('PUM')
    value[0], value[1], value[2] = value[0] + 4, value[1] + 4, value[2] + 4
"""
import sys


class recursionlimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)


def recursion(n, a=1, b=2, c=3, counter=0, d="PUM"):
    print("%i %i %i %s" % (a, b, c, d))
    a += 4
    b += 4
    c += 4
    counter += 1
    if n == counter:
        return 0
    recursion(n, a, b, c, counter, d)


with recursionlimit(50000):
    recursion(int(input()))