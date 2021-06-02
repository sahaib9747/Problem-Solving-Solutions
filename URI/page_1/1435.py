from math import ceil
while True:
    userInput = int(input())
    if userInput == 0:
        break
    else:
        arr = [[1 for j in range(userInput)] for i in range(userInput)]  # create 2D array with default value 1
        layer = ceil(userInput / 2)
        for selectLayer in range(1, layer):  # select the layer
            row = selectLayer
            maxRowCol = userInput - selectLayer
            for selectRow in range(row, maxRowCol):  # select row
                col = selectLayer
                for column in range(col, maxRowCol):  # select col and change the value
                    arr[selectRow][column] = selectLayer + 1
        for row in range(userInput):
            for col in range(userInput):
                if col == 0:
                    print("  %i" % arr[row][col], end="")
                else:
                    if arr[row][col] >= 10:
                        print("  %i" % arr[row][col], end="")
                    else:
                        print("   %i" % arr[row][col], end="")
            print()
        print()