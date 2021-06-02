checkAv = lambda totalValue, totalPerson: "%.2f" % (totalValue / totalPerson)
counter = 0
def takeInput(value = 0):
    global counter
    age = int(input())
    if age < 0:
        return 0
    elif age == 0:
        counter += 0
    else:
        value = age
        counter += 1
    return value + takeInput()
print(checkAv(takeInput(), counter))