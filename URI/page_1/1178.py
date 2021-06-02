value = float(input())
array = [False] * 100


def alter(arr, value, index=0):
    if index == 100:
        return arr
    arr[index] = "N[%i] = %.4f" % (index, value)
    index += 1
    value /= 2
    return alter(arr, value, index)


alter(array, value)
print(*array, sep='\n')