import sys


def readFile(array):  # until end of file -> EOF
    array.extend(map(int, sys.stdin))
    return array


def processResult(inputArr,arr, length, index=0):
    if length == index:
        return arr
    else:
        if inputArr[index]:
            arr.append("vai ter duas!")
        else:
            arr.append("vai ter copa!")
    index += 1
    return processResult(inputArr, arr, length, index)


def main():
    inputArray = []
    result = []
    readFile(inputArray)
    processResult(inputArray, result, len(inputArray))
    print(*result, sep="\n")


if __name__ == '__main__':
    main()
