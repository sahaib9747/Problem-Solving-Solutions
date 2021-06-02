aCode, aUnit, aPrice = map(float, input().split())
bCode, bUnit, bPrice = map(float, input().split())
print("VALOR A PAGAR: R$ %.2f" % ((aUnit * aPrice) + (bUnit * bPrice)))