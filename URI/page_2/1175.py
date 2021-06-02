data = [int(input()) for i in range(20)]
data.reverse()
for i,j in enumerate(data):
    print("N[%i] = %i" % (i, j))