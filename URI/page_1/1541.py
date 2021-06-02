from math import sqrt


def readFile(array):
    userInput = list(map(int, input().split()))
    if sum(userInput) == 0:
        return array
    else:
        array.append(userInput)
    return readFile(array)


def findSquareLand(houseSize, totalLand, percent):
    square = sqrt(houseSize) / sqrt((totalLand / 100 * percent)) * totalLand
    return int(square)


def display(array):
    print(*array, sep='\n')


def process(inputArr, length, row=0, col=0, displayArr=[]):
    if length == row:
        return display(displayArr)  # this will go to display()
    else:
        # this will find the SquareLand
        displayArr.append(findSquareLand(inputArr[row][col], inputArr[row][col+1], inputArr[row][col+2]))
    row += 1
    return process(inputArr, length, row, col, displayArr)


def main():
    userInput = []
    readFile(userInput)
    process(userInput, len(userInput))


if __name__ == '__main__':
    main()
