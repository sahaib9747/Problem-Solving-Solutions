def matSum(array, row=1, col=0, diagonalSum=0):  # this function will find out the sum.
    if row == 12:
        return 0
    elif col == row:
        row += 1
        col = 0
    else:
        diagonalSum = array[row][col]
        col += 1
    return diagonalSum + matSum(array, row, col)


operation = input().upper()
arr = [[float(input()) for j in range(12)] for i in range(12)]  # creating 2D Array.
if operation == 'S':
    print("%.1f" % matSum(arr))
else:
    print("%.1f" % (matSum(arr) / 66))

