def simple(p, y, r):
    total = (p / 100 * r) * y
    return total

def compound(p, y, r):
    total = p * ((1 + r /100) ** y) - p
    return total

def main():
    inp = int(input())

    for i in range(inp):
        p, y, r1, r2 = list(map(int, input().split()))

        b1 = simple(p, y, r1)
        b2 = compound(p, y, r2)

        if b1 < b2:
            print('Bank 1')
        elif b2 < b1:
            print('Bank 2')
        else:
            print('Confused huh!')

main()