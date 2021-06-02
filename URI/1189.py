import sys

def leftArea(arr, row=1, col=0, diagonalSum=0):
    if col == 5:
        return diagonalSum
    elif row == 11 - col:
        col += 1
        row = col + 1
    else:
        diagonalSum = arr[row][col]
        row += 1
    return diagonalSum + leftArea(arr, row, col)


def main():
    opCode = input().upper()  # operation code
    array = [[float(sys.stdin.readline().strip()) for j in range(12)] for i in range(12)]
    if opCode == 'S':
        print('%.1f' % leftArea(array))
    else:
        print('%.1f' % (leftArea(array) / 30))


main()
