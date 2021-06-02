child, choco = map(int, input().split())

if choco % child == 0:
    print(0)
else:
    way1 = 1
    way2 = 1
    while True:
        if (choco + way1) % child == 0:
            break
        way1 += 1
    print(way1)

