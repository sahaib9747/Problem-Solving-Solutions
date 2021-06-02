sum = 0
x = int(input())
y = int(input())
if x > y:
    y, x = x, y
for i in range(x, y+1):
    if i % 13 != 0:
        sum += i
print(sum)