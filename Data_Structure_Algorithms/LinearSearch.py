"""
Linear Search is a straight forward searching algorithm, It searches in source by index 0 to N sequentially.
"""

def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return(True, i)

    return False, -1

lst = [10, 20, 30, 10, 50, 'cefalo', 'bjit', 'datasoft', 'bs-23']

status, position = linear_search(lst, 'datasoft')

print(f"Searching Status: {status} and Postion {position}")