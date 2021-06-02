def div(val, n=1, divisor=[]):
    if n == val:
        return [val]
    if val % n == 0:
        divisor = [n]
    else:
        divisor = []
    n += 1
    return divisor + div(val, n)


print(*div(int(input())), sep="\n")