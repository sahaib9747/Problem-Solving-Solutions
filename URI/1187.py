def topArea(array, row=0, col=1, topSum=0):
    if row == 5:
        return topSum
    elif col == (11 - row):
        row += 1
        col = (row + 1)
    else:
        topSum = array[row][col]
        col += 1
    return topSum + topArea(array, row, col)


op = input().upper()
arr = [[float(input()) for col in range(12)] for row in range(12)]

if op == 'S':
    print('%.1f' % topArea(arr))
else:
    print('%.1f' % (topArea(arr) / 30))