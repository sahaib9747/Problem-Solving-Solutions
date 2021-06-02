import sys


def createMatrix(arr, row, col=2, counter=0):
    if counter == row:
        return arr
    createMat = [False] * col
    arr.append(createMat)
    counter += 1
    return createMatrix(arr, row, col, counter)


def fillData(arr, length, row=0):
    if row == length:
        return arr
    else:
        arr[row][0], arr[row][1] = map(lambda x: int(x), sys.stdin.readline().strip().split())
    row += 1
    return fillData(arr, length, row)


def makeResult(arr, result, length, row=0):
    if row == length:
        return result
    else:
        result.append(sum(arr[row]))
    row += 1
    return makeResult(arr, result, length, row)


def main():
    array = []
    result = []
    length = int(sys.stdin.readline().strip())
    createMatrix(array, length)
    fillData(array, length)
    makeResult(array, result, length)
    print(*result, sep='\n')


if __name__ == '__main__':
    sys.setrecursionlimit(3500)
    main()
