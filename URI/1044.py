a,  b = map(int, input().split())
a , b = abs(a), abs(b)
if a > b:
    b,a = a,b
multipleChecker = lambda a, b: (b % a == 0)
if multipleChecker(a, b):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")