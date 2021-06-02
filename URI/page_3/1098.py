from math import ceil

i = 0
for n in range(11):
    j = i + 1
    for k in range(3):
        if i == 0 or i == 1 or i > 1.8:
            print("I=%i J=%i" % (ceil(i), j))
        else:
            print("I=%.1f J=%.1f" % (i, j))
        j += 1
    i += 0.2