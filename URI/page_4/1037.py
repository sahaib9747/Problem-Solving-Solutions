msg = ["Intervalo [0,25]", "Intervalo (25,50]", "Intervalo (50,75]", "Intervalo (75,100]", "Fora de intervalo"]
a = float(input())
conChecker = [a >= 0.00 and a <= 25, a > 25.00 and a <= 50.00, a > 50.00 and a <= 75.00, a > 75.00 and a <= 100.00, a < 0.00 or a > 100.00]
print(msg[conChecker.index(True)])