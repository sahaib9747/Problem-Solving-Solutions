def selectionSort(array):
    for i in range(len(array) - 1):
        minIndex = i
        for j in range(i + 1 , len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        if array[minIndex] < array[i]:
            temp = array[i]
            array[i] = array[minIndex]
            array[minIndex] = temp
    return array
array = list(map(int, input().split()))
x = []
x = array.copy()
selectionSort(array)
for i in array:
    print(i)
print()
for i in x:
    print(i)