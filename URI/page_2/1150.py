x, z = int(input()), int(input())
while x >= z:
    z = int(input())
total, count = 0, 0
if x < 0:
    total = x
while z > total:
    total += x + count
    count += 1
print(count)