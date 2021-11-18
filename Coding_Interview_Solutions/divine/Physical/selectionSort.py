def selectionsort(lst):
    for i in range(len(lst)):
        smallest = lst[i]
        for j in range(j+1, len(lst)):
            if lst[j] < smallest:
                lst[i], lst[j] = lst[j], lst[i]
                smallest = lst[i]
            
