import sys
from math import ceil


def readFile(arr):
    arr.extend((map(int, sys.stdin)))  # read file until EOF
    return arr


def createMatrix(arr, length, mid, mainDia, row=0, secondPart=0):
    if row == length:
        return arr
    else:
        if row < mainDia:
            if row == 0:
                createRow = '2' + ('0' * (length-2)) + '3'
                arr.append(list(map(int, createRow)))
            else:
                newRow = arr[row-1].copy()
                newRow[row-1], newRow[row] = newRow[row], newRow[row - 1]
                newRow[length-row], newRow[length-row-1] = newRow[length-row-1], newRow[length-row]
                arr.append(newRow)
        else:
            if row == mid - 1:
                newRow = arr[row-1].copy()
                newRow[mid-1] = 4
                arr.append(newRow)
            elif row < mid - 1:
                if secondPart == 0:
                    one = length - (mainDia * 2)
                    createRow = '0' * mainDia + '1' * one + '0' * mainDia
                    arr.append(list(map(int, createRow)))
                    secondPart += 1
                else:
                    arr.append(arr[row-1])
            else:
                index = length - row - 1
                newRow = arr[index].copy()
                newRow.reverse()
                arr.append(newRow)
    row += 1
    return createMatrix(arr, length, mid, mainDia, row, secondPart)


def display(arr, length, row=0):
    if row == length:
        print()
        return 0
    else:
        print(''.join(map(str, arr[row])))
    row += 1
    return display(arr, length, row)


def doWork(inputFile, length, row=0):
    if length == row:
        return 0
    else:
        arr = []  # Create a empty array
        mid = ceil(inputFile[row] / 2)
        mainDia = inputFile[row] // 3
        createMatrix(arr, inputFile[row], mid, mainDia)  # create and update a matrix
        display(arr, inputFile[row])  # display() it
    row += 1
    return doWork(inputFile, length, row)


def main():
    inputFile = []
    readFile(inputFile)  # read the file from user
    doWork(inputFile, len(inputFile))


if __name__ == '__main__':
    main()

