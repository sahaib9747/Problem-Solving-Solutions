def selectionSort(array):
    # descending order
    length = len(array)
    for i in range(length - 1):
        maxIndex = i
        for j in range(i + 1, length):
            if array[j] > array[maxIndex]:
                maxIndex = j
        if array[maxIndex] > array[i]:
            temp = array[i]
            array[i] = array[maxIndex]
            array[maxIndex] = temp
    return array


array = selectionSort(list(map(float, input().split())))
a, b, c = array

display = ["NAO FORMA TRIANGULO", "TRIANGULO RETANGULO", "TRIANGULO OBTUSANGULO", "TRIANGULO ACUTANGULO",
           "TRIANGULO EQUILATERO", "TRIANGULO ISOSCELES"]
conChecker = lambda a, b, c: (
[a >= b + c, a ** 2 == b ** 2 + c ** 2, a ** 2 > b ** 2 + c ** 2, a ** 2 < b ** 2 + c ** 2, a == b == c,
 a == b != c or a != b == c or a == c != b])
checker = conChecker(a, b, c)
print(display[checker.index(True)])
if checker[4] or checker[5]:
    print(display[checker.index(True, 4)])