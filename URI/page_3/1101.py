display = []
checker = lambda a, b: (b, a) if b > a else (a, b)
while True:
    x, y = map(int, input().split())
    if x <= 0 or y <= 0:
        break
    else:
        sum = 0
        x, y = checker(x, y)
        for i in range(y, x + 1):
            sum += i
            print(i, end=" ")
        print("Sum=%i" % sum)