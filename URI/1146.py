inputValues = []
display = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        inputValues.append(n)
for i in range(len(inputValues)):
    temp = ""
    for j in range(1, inputValues[i] + 1):
        if j != inputValues[i]:
            temp += str(j) + " "
        else:
            temp += str(j)
    display.append(temp)
print(*display, sep="\n")