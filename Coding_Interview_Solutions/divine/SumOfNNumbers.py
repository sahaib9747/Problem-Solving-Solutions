num = int(input())
# formula: n * n-1 // 2
total = (lambda n: (n * (n-1)) // 2)(num)
print(total)
