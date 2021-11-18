def checkYear(arr):
    for i in range(4):
        for j in range(i+1, 4):
            if arr[i] == arr[j]:
                return 0
    return 1
 
 
# input
year = int(input()) + 1

while True:
    if checkYear(str(year)):
        print(year)
        break
    year += 1