line = int(input())
operation = input().upper()


def sumOfArray(arr, col):
    Sum = 0
    for i in range(12):
        Sum += arr[i][col]
    return Sum


def averageOfArray(func, arr, col):
    div = sum([1 for i in range(12) if arr[i][col] > 0 or arr[i][col] < 0])
    if div == 0:
        return 0
    else:
        return func(arr, col) / div


matrix = [[float(input()) for i in range(12)] for i in range(12)]

if operation == 'M':
    print("%.1f" % averageOfArray(sumOfArray, matrix, line))
elif operation == 'S':
    print("%.1f" % sumOfArray(matrix, line))
