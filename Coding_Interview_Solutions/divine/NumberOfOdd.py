n = 101

result = 0
if n % 2 != 0:
    result = 1

result += (lambda x: x // 2)(n)

print(result)
