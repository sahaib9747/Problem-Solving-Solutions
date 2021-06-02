def recursion(i = 1,j = 60):
    print("I=%i J=%i" % (i,j))
    if j == 0:
        return 0
    i += 3
    j -= 5
    recursion(i , j)

    
recursion()