def readFile(arr, tCase, row=0):
    if row == tCase:
        return arr
    else:
        arr.append(input().lower().split())
    row += 1
    return readFile(arr, tCase, row)


def makeResult(inputArray, judgeArray, outputArray, tCase=1):
    if tCase > len(inputArray):
        return outputArray
    elif inputArray[tCase-1][0] == inputArray[tCase-1][1]:
        outputArray.append("Caso #%i: De novo!" % tCase)
    elif inputArray[tCase-1] in judgeArray:
        outputArray.append("Caso #%i: Bazinga!" % tCase)
    else:
        outputArray.append("Caso #%i: Raj trapaceou!" % tCase)
    tCase += 1
    return makeResult(inputArray, judgeArray, outputArray, tCase)


def display(arr):
    print(*arr, sep='\n')


def main():
    judgeArray = [['tesoura', 'papel'], ['papel', 'pedra'],
           ['pedra', 'lagarto'], ['lagarto', 'spock'],
           ['spock', 'tesoura'], ['tesoura', 'lagarto'],
           ['lagarto', 'papel'], ['papel', 'spock'],
           ['spock', 'pedra'], ['pedra', 'tesoura']]
    inputFile = []
    testCase = int(input())
    readFile(inputFile, testCase)
    displayArray = []
    makeResult(inputFile, judgeArray, displayArray)
    display(displayArray)


if __name__ == '__main__':
    main()
