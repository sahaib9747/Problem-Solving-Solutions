import sys

def matSum(arr, row=5, col=7, diagonalSum=0):
    if col == 12:
        return diagonalSum
    elif row == col:
        col += 1
        row = 11 - col + 1
    else:
        diagonalSum = arr[row][col]
        row += 1
    return diagonalSum + matSum(arr, row, col)


def main():
    opCode = input().upper()  # operation code
    array = [[float(sys.stdin.readline().strip()) for j in range(12)] for i in range(12)]
    if opCode == 'S':
        print('%.1f' % matSum(array))
    else:
        print('%.1f' % (matSum(array) / 30))


main()
