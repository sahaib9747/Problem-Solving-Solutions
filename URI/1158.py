tCase = int(input())
for i in range(tCase):
    x, y = map(int, input().split())
    totalSum = 0
    n = 0
    while( n != y):
        if x % 2 == 0:
            x += 1
        else:
            totalSum += x
            x+=2
            n += 1
    print(totalSum)