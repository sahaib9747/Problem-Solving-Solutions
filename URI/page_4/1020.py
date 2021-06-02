msg = ["ano(s)", "mes(es)", "dia(s)"]
divisor = [365, 30, 1]
ageCalculator = lambda x, divisor: (x / divisor, x % divisor)
days = int(input())
for i in range(3):
    display, days = ageCalculator(days, divisor[i])
    print("%i %s" % (display, msg[i]))