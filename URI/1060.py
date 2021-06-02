userInput = [float(input()), float(input()), float(input()), float(input()), float(input()), float(input())]
counter = lambda lst: [0 <= lst[0], 0 <= lst[1], 0 <= lst[2], 0 <= lst[3], 0 <= lst[4], 0 <= lst[5]]
checker = counter(userInput)
print("%i valores positivos" % checker.count(True))