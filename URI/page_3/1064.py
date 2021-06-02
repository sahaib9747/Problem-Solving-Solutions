sum = 0
positive = 0
for i in range(6):
    user = float(input())
    if user > 0:
        sum += user
        positive += 1
print("%i valores positivos\n%.1f" % (positive, sum / positive))