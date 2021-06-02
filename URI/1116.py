tCase = [list(map(int, input().split())) for i in range(int(input()))]
display = []
for lst in tCase:
    x, y = lst
    if y == 0:
        display.append("divisao impossivel")
    else:
        display.append("%.1f" % (x / y))
print(*display, sep="\n")