i, j = 1, 7
for n in range(1, 6):
    f = j
    for k in range(3):
        print("I=%i J=%i" % (i, f))
        f -= 1
    i += 2
    j += 2