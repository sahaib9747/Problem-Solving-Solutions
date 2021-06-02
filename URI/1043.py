a, b , c = map(float , input().split())
triagle = lambda a, b, c: True if a + b > c and b + c > a and a + c > b else False
trapeium = lambda a, b, c: (a + b) / 2 * c
perimeter = lambda a, b ,c: a + b + c

if triagle(a, b, c):
    print("Perimetro = %.1f" % perimeter(a, b, c))
else:
    print("Area = %.1f" % trapeium(a, b, c))