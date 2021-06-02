from math import ceil
import sys


def readFile(array):
    array.extend(map(lambda x: int(x), sys.stdin))
    return array


def createMatrix(arr, length, row=0):
    if row == length:
        return arr
    else:
        if row == 0:
            createRow = ['3'] * length
            arr.append(createRow)
        else:
            arr.append([])
        row += 1
    return createMatrix(arr, length, row)


def updateMatrix(arr, length, limit, row=0, leftCol=0, rightCol=0):
    if row == length:
        return arr
    else:
        if row < limit:
            if row == 0:
                arr[0][0] = '1'
                arr[0][-1] = '2'
                leftCol = length - 1
                rightCol = 0
            else:
                arr[row].extend(arr[row - 1])
                if rightCol + 1 == leftCol - 1:
                    arr[row][rightCol] = '3'
                    arr[row][leftCol], arr[row][leftCol - 1] = arr[row][leftCol - 1], arr[row][leftCol]
                else:
                    arr[row][rightCol], arr[row][rightCol + 1] = arr[row][rightCol + 1], arr[row][rightCol]
                    arr[row][leftCol], arr[row][leftCol - 1] = arr[row][leftCol - 1], arr[row][leftCol]
                    rightCol += 1
                    leftCol -= 1
        else:
            reverseRow = arr[length - row - 1].copy()
            reverseRow.reverse()
            arr[row].extend(reverseRow)
    row += 1
    return updateMatrix(arr, length, limit, row, leftCol, rightCol)


def display(arr, length, row=0):
    if row == length:
        return 0
    else:
        print(''.join(arr[row]))
        row += 1
    return display(arr, length, row)


def work(array, lenArray, count=0):
    if lenArray == count:
        return 0
    else:
        length = array[count]
        createLimit = ceil(length / 2)  # after this limit no swapping will happen, only do reversing
        arr = []
        createMatrix(arr, length)
        updateMatrix(arr, length, createLimit)
        display(arr, length)
        count += 1
    return work(array, lenArray, count)


def main():
    userInput = []
    readFile(userInput)
    work(userInput, len(userInput))


main()
