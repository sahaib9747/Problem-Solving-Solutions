import sys


def readFile(proArr, arr=[]):
    arr.extend(sys.stdin)
    return processFile(arr, proArr, len(arr))


def processFile(arr, proArr, length, index=1):
    if index >= length:
        return proArr
    else:
        proArr.append(max(list(map(lambda i: int(i), arr[index].split()))))
    index += 2
    return processFile(arr, proArr, length, index)


def makeResult(arr, result, length, index=0):
    if index == length:
        return result
    else:
        result.append(1 if 10 > arr[index] else 2 if 10 <= arr[index] < 20 else 3)
    index += 1
    return makeResult(arr, result, length, index)


def display(arr):
    print(*arr, sep='\n')


def main():
    inputFile = []
    readFile(inputFile)  # processed file
    result = []
    makeResult(inputFile, result, len(inputFile))
    display(result)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    main()
