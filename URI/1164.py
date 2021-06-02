def pNumber(num, increment=1):
    Sum = 0
    if num % 2 == 0:
        while increment <= (num // 2):
            if num % increment == 0:
                Sum += increment
            increment += 1
    return Sum


msg = ["nao eh perfeito", "eh perfeito"]
tCase = int(input())
display = []
for i in range(tCase):
    x = int(input())
    if pNumber(x) == x:
        display.append("%i eh perfeito" % x)
    else:
        display.append("%i nao eh perfeito" % x)
print(*display, sep="\n")