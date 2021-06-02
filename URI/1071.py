x, y = int(input()), int(input())
sum = 0
swap = lambda x, y: (y, x) if y > x else (x, y)
x, y = swap(x,y)
y = (lambda b: b + 1 if b % 2 == 0 else (((b + 2) if b % 2 != 0 else b+0)))(y)
for i in range(y, x, 2):
    sum += i
print(sum)