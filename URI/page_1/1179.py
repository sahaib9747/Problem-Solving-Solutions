evenArray = []
oddArray = []
display = []

def evenPrinter(arr, counter=0):
    if counter == 5 or arr == []:
        return arr
    else:
        display.append("par[%i] = %i" % (counter, arr[0]))
        arr.pop(0)
        counter += 1
    return evenPrinter(arr, counter)


def oddPrinter(arr, counter=0):
    if counter == 5 or arr == []:
        return arr
    else:
        display.append("impar[%i] = %i" % (counter, arr[0]))
        arr.pop(0)
        counter += 1
    return oddPrinter(arr, counter)


for i in range(15):
    userInput = int(input())
    if userInput % 2 == 0:
        evenArray.append(userInput)
        if len(evenArray) == 5:
            evenPrinter(evenArray)
    else:
        oddArray.append(userInput)
        if len(oddArray) == 5:
            oddPrinter(oddArray)
oddPrinter(oddArray)
evenPrinter(evenArray)

print(*display, sep="\n")