product = ["Alcool", "Gasolina", "Diesel"]
userInput = [0, 0, 0]
while True:
    n = int(input())
    if n < 4:
        quantity = (lambda x: [x == 1, x == 2, x == 3])(n)
        userInput[quantity.index(True)] += 1
        continue
    if n == 4:
        break
print("MUITO OBRIGADO")
for j in range(3):
    print("%s: %i" % (product[j], userInput[j]))