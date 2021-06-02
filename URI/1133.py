x = int(input())
y = int(input())
if x > y:
    y, x = x, y
for i in range(x+1, y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)