arr = [int(input()) for i in range(10)]
for i,j in enumerate(arr):
    j = j if j > 0 else 1  
    print('X[%i] = %i' % (i , j))