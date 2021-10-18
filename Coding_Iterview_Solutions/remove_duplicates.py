"""
-You have a sorted list
-the list has duplicate values,
-you have to remove them and return the length
-you can't consume more space
"""

lst = [10, 20, 30, 40, 50, 10, 70, 40, 30, 50]
lst.sort() # a sorted list

def remove_duplicates(lst):
    for index in range(1, len(lst)):
        if index < len(lst) and lst[index] == lst[index-1]:
            lst.remove(lst[index])
        elif index == len(lst):  # we don't have to iterate N(length of list) time cause length will reduce after removing items
            break 

    return len(lst)


print(f"Before remvoing items: {lst} and length: {len(lst)}")
print(f"After remvoing: length: {remove_duplicates(lst)} and list: {lst}")