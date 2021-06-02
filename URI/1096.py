i, j = 1, 7
for n in range(15):
    print("I=%i J=%i" % (i, j))
    if j == 5:
        j = 7
        i += 2
    else:
        j -= 1