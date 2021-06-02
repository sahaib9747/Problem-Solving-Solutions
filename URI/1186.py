def matSum(arr, row=1, col=11, diagonalSum=0):
    if row == 12:
        return diagonalSum
    elif col == 12:
        row += 1
        col = 11 - (row - 1)
    else:
        diagonalSum = arr[row][col]
        col += 1
    return diagonalSum + matSum(arr, row, col)


operation = input().upper()
array = [[float(input()) for j in range(12)] for i in range(12)]

if operation == 'S':
    print('%.1f' % matSum(array))
else:
    print('%.1f' % (matSum(array) / 66))
