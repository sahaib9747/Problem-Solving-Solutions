x, y = map(int, input().split())
counter = 1
for i in range(1, y+1):
    if counter == x:
        print("%i" % i)
        counter = 1
    else:
        print("%i " % i, end="")
        counter += 1