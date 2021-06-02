a, b, c, d = map(int, input().split())
conChecker = [b > c and d > a, (c + d) > (a + b), c >= 0 and d >= 0, a % 2 == 0]
if all(conChecker):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")