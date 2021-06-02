import math
number = int(input())
div = []
for i in range(1, int(math.sqrt(number)) + 1):
    if number % i == 0:
        if number // i == i:
            div.append(i)
        else:
            div.extend([i, number//i])
print(*sorted(div), sep='\n')