#Bhaskar's formula to determine roots of x1,x2

bhaskarFormulaR1 = lambda a, b, d: (- b + (d ** .5)) / (2 * a)
bhaskarFormulaR2 = lambda a, b, d: (- b - (d ** .5)) / (2 * a)
a, b, c = map(float, input().split())

try:
    d = b ** 2 - 4 * a * c
    if d > 0:
        print("R1 = %.5f\nR2 = %.5f" % (bhaskarFormulaR1(a, b, d), bhaskarFormulaR2(a, b, d)))
    else:
        print("Impossivel calcular")
except ZeroDivisionError:
    print("Impossivel calcular")