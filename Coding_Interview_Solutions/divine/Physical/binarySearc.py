def binarySearch(lst, item):
    start = 0
    end = len(lst)-1
    mid = end // 2
    left, right = 0, len(lst)
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == item:
            return item
        if lst[mid] > item:
            right = mid -1
        elif lst[mid] < item:
            right = mid+1
    return -1
        

n = [20,30,40,50,60,70]

print(binarySearch(n, 10))