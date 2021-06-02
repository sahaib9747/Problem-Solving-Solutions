def sumOfOddValues(x,y):
    if y > x:
        x, y = y, x
    sum = 0
    y = checker(y)
    for i in range(y, x, 2):
        sum += i
    return sum
checker = lambda a: a+1 if a % 2 == 0 else a+2
tCase = int(input())
display = [False] * tCase
for i in range(tCase):
    x, y = map(int, input().split())
    display[i] = sumOfOddValues(x, y)
print(*display, sep="\n")