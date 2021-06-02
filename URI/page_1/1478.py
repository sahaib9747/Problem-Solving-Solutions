import sys


def readFile(arr):
    userInput = sys.stdin.readline().strip()
    if userInput == '0':
        return arr
    else:
        arr.append(int(userInput))
    return readFile(arr)


def createMatrix(arr, dimen, counter=0):  # dimen-> dimension
    if counter == dimen:
        return arr
    else:
        if counter == 0:
            row = [False] * dimen
            arr.append(row)
        else:
            row = [False] * 1
            arr.append(row)
        counter += 1
    return createMatrix(arr, dimen, counter)


def updateMatrix(arr, length, row=0, col=0):
    if row == length:
        return arr
    elif row < length:
        if row != 0:
            preArrayRow = row - 1
            if col == 0:
                arr[row][col] = (' %i' % (row + 1)) if 10 <= row + 1 <= 99 else \
                    ("100" if row + 1 == 100 else '  %i' % (row + 1))
                if col == length - 1:
                    col = -1
                    row += 1
            else:
                arr[row].append(" %s" % arr[preArrayRow][col-1])
                arr[row].extend(arr[preArrayRow][1:-1])
                col = -1
                row += 1
        else:
            if col == 0:
                arr[row][col] = (' %i' % (col + 1)) if 10 <= col + 1 <= 99 else \
                    ("100" if col + 1 == 100 else '  %i' % (col + 1))
                if col == length - 1:
                    col = -1
                    row += 1
            else:
                arr[row][col] = ('  %i' % (col + 1)) if 10 <= col + 1 <= 99 else \
                    " 100" if col + 1 == 100 else '   %i' % (col + 1)
                if col == length - 1:
                    col = -1
                    row += 1
    col += 1
    return updateMatrix(arr, length, row, col)


def displayMatrix(arr, length, row=0, col=0):
    if row == length:
        print()
        return 0
    else:
        print(''.join(arr[row]))
    row += 1
    return displayMatrix(arr, length, row)


def finalWork(arr, length, indexCount=0):
    if indexCount == length:
        return 0
    else:
        matrix = []  # Create a 2D Matrix
        createMatrix(matrix, arr[indexCount])  # this function will create a matrix
        updateMatrix(matrix, arr[indexCount])  # update elements
        displayMatrix(matrix, arr[indexCount])  # it will display all of the elements
    indexCount += 1
    return finalWork(arr, length, indexCount)


def main():
    userInput = []
    readFile(userInput)
    finalWork(userInput, len(userInput))

main()
