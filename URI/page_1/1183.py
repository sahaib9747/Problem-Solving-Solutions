import sys


def matrixSum(arr, row=0, col=1, diagolSum=0):
    if row == 11:
        return diagolSum
    elif col == 12:
        row += 1
        col = row + 1
    else:
        diagolSum = arr[row][col]
        col += 1
    return diagolSum + matrixSum(arr, row, col)


operation = input().upper()
array = [[float(sys.stdin.readline().strip()) for j in range(12)]for i in range(12)]
if operation == 'S':
    print('%.1f' % matrixSum(array))
else:
    print('%.1f' % (matrixSum(array) / 66))