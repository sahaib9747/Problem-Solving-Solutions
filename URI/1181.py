line = int(input())
operation = input().upper()


def sumOfArray(arr, lines):
    print("%.1f" % sum(arr[lines]))


def averageOfArray(arr, lines):
    div = sum([1 for i in arr[lines] if i > 0 or i < 0])
    if div == 0:
        print(0.0)
    else:
        print("%.1f" % (sum(arr[lines]) / div))


matrix = [[float(input()) for i in range(12)] for i in range(12)]

if operation == 'M':
    averageOfArray(matrix, line)
elif operation == 'S':
    sumOfArray(matrix, line)