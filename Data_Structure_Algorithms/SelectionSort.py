"""
This algorithm will sort a array in a easier way
It will selct a item then compare with others, if it is smallest
then item will be placed in the first. 
the process will be remain. 
"""

def selection_sort(lst):
    for i in range(len(lst)-1):
        smallest = i 
        for j in range(i+1, len(lst)):
            if lst[j] < lst[smallest]:
                lst[j], lst[smallest] = lst[smallest], lst[j]
    return lst

arr = [10, 1, 2, 4,6, 5, 9, 7]

print(selection_sort(arr))