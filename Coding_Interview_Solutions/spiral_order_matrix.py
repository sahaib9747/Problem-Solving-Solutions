matrix = [
    [1, 2, 3, 0],
    [4, 5, 6, 0],
    [7, 8, 9, 0],
    [7, 8, 9, 0],
]

lst  = []


def spiral(mat):
    global lst
    m = len(mat)
    n = len(mat[0])

    if m >= 2 and n >= 1:
        for mi in range(2):
            if mi == 0:
                for ni in range(n):
                    lst.append(matrix[mi][ni])
                inner = m - 2
                if inner:
                    for x in range(m-2, mi, -1):
                        lst.append(matrix[x][ni])
                        matrix[x].pop(ni)
            else:
                mi = m-1
                for ni in range(n-1,-1, -1):
                    lst.append(matrix[mi][ni])
                
                inner = m-2
                if inner:
                    for x in range(m-2, 0, -1):
                        lst.append(matrix[x][0])
                        matrix[x].pop(0)
        matrix.pop(0)
        matrix.pop(-1)
        m -= 2
        n -= 2
        
    elif m == 1 and n: 
        return lst.extend(*matrix)
        m = 0

    if not m:
        return
    
    return spiral(matrix)
    

spiral(matrix)
print(lst)
