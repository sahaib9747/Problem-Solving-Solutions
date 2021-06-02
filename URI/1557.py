import sys

parseInt = lambda value: int(value.strip()) * 2

updateElement = lambda element, space: ' ' * (space - 1) + str(element) if 10 <= element <= 99 else \
    ' ' * (space - (len(str(element)) - 1)) + str(element) if element >= 100 else ' ' * space + str(element)


def readFile(arr):
    userInput = sys.stdin.readline()  # read input
    if userInput.strip() == '0':
        return arr
    else:
        arr.append(int(userInput))
    return readFile(arr)


def createMatrix(arr, dimen, row=0, col=0, createRow=[], space=0):
    if dimen == row:
        return arr
    else:
        if row == 0:
            if col == dimen:
                arr.append(createRow)
                row += 1
                col = 0
            elif col == 0:
                space = len(str((2 ** (dimen - 1)) ** 2))  # space counter
                createRow = [1] * dimen  # create space for dimension -1 elements.
                createRow[0] = ' ' * (space - 1) + '1'  # space
            else:
                element = parseInt(createRow[col - 1])  # value -> # convert int 2x of previous col
                createRow[col] = updateElement(element, space)  # calling lambda expressions
            col += 1
        else:
            # 2x of previous row
            element = parseInt(arr[row - 1][0])
            rowFirstElements = [' ' * (space - 1) + str(element) if element < 10 else \
                                    ' ' * (space - 2) + str(element) if 10 <= element <= 99 else \
                                        ' ' * (space - (len(str(element)))) + str(element)]
            arr.append(rowFirstElements + list(map(lambda x: updateElement(parseInt(x), space), arr[row - 1][1:])))
            row += 1
    return createMatrix(arr, dimen, row, col, createRow, space)


def display(arr, dimen, row=0):
    if row == dimen:
        print()
        return 0
    else:
        print(''.join(arr[row]))
    row += 1
    return display(arr, dimen, row)


def finalWork(userArr, length, index=0):
    if index == length:
        return 0
    else:
        array = []
        createMatrix(array, userArr[index])
        display(array, userArr[index])
    index += 1
    return finalWork(userArr, length, index)


def main():
    userInput = []
    readFile(userInput)
    finalWork(userInput, len(userInput))


if __name__ == '__main__':
    main()
