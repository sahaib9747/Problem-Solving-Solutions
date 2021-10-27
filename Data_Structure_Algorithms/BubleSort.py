def buble_sort(lst: list):
    for i in range(len(lst)-1):
        for j in range(0, len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = [10, 1, 9, 4, 5, 7, 10]

print(buble_sort(lst))