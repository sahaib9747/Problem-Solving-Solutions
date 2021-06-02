rectTri = lambda a, c: a * c * .5
circle = lambda c: 3.14159 * c ** 2
trap = lambda a, b, c: (a + b) / 2 * c
square = lambda b: b ** 2
rect = lambda a, b: a * b
def main():
    a, b, c = map(float, input().split())
    print("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f" % (
    rectTri(a, c), circle(c), trap(a, b, c), square(b), rect(a, b)))
main()