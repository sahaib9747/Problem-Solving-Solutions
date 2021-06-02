display = []
conditionCheck = lambda x: True if 0 <= x <= 10 else False
storeInput = []

while True:
    userInput = float(input())
    if conditionCheck(userInput):
        if len(storeInput) <= 2:
            storeInput.append(userInput)
            if len(storeInput) == 2:
                break
    else:
        display.append("nota invalida")
        continue

display.append("media = %.2f" % ((storeInput[0] + storeInput[1]) / 2))
print(*display, sep="\n")