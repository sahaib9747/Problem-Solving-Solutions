def matSum(arr, row=7, col=5, diagonalSum=0):
    if row == 12:
        return diagonalSum
    elif col == row:
        row += 1
        col = 11 - row + 1
    else:
        diagonalSum = arr[row][col]
        col += 1
    return diagonalSum + matSum(arr, row, col)


def main():
    opCode = input().upper()  # operation code
    array = [[float(input()) for i in range(12)] for j in range(12)]
    if opCode == 'S':
        print('%.1f' % matSum(array))
    else:
        print('%.1f' % (matSum(array) / 30))


main()
