tcase = int(input())

for i in range(1,tcase+1):
    space = tcase - i - 1
    if i != tcase:
        print(" " * space + " *" * i)
    else:
        print(*list("*" * i), sep=" ")