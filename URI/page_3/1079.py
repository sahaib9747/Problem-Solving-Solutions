avCalculator = lambda a, b, c: (a * 2 + b * 3 + c * 5) / 10
tCase = int(input())
for i in range(tCase):
    a, b, c = map(float, input().split())
    print("%.1f" % avCalculator(a, b, c))