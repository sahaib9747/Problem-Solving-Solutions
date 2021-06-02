conditionCheck = lambda x: True if 0 <= x <= 10 else False


def avCounter(dispaly, storeInput):
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
    print("novo calculo (1-sim 2-nao)")


storeInput = []
display = []
avCounter(display, storeInput)

while True:
    x = int(input())
    if x > 2 or x < 1:
        print("novo calculo (1-sim 2-nao)")
        continue
    else:
        if x == 1:
            storeInput = []
            display = []
            avCounter(display, storeInput)
            continue
        else:
            break
