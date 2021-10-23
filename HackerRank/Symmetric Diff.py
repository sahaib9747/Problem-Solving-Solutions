import sys

n = sys.stdin.readlines()
a = set(map(int, n[1].split()))
b = set(map(int, n[3].split()))

print(len(a.symmetric_difference(b)))
