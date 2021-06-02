def even(x, y = 5, counter=0):
    if counter == y:
        return 0
    if x % 2 == 0:
        Sum = x
        counter += 1
        x += 2
    else:
        Sum = 0
        x += 1
    return Sum + even(x, y, counter)

display = []
while(True):
    userInput = int(input())
    if userInput == 0:
        break
    display.append(even(userInput))
print(*display, sep='\n')