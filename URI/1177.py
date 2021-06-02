import sys


class recursionLimit:
    def __init__(self, limit):
        self.limit = limit

    def __enter__(self):
        sys.setrecursionlimit(self.limit)
    
    def __exit__(a, b, c, d):
        sys.setrecursionlimit(1000)


def ref(data, val, index=0, counter=0):
    if index == 1000:
        return data
    if counter == len(val):
        counter = 0
    data[index] = val[counter]
    counter += 1
    index += 1
    return ref(data, val, index, counter)


with recursionLimit(1200):
    data = [False] * 1000
    val = int(input())
    val = [i for i in range(val)]
    ref(data, val)
    for i, j in enumerate(data):
        print("N[%i] = %i" % (i, j))