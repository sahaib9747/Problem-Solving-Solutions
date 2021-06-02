x = list(map(int, input().split()))
inputValues = []
for i in x:
    if len(inputValues) == 1 and i > 0:
        inputValues.append(i)
    elif len(inputValues) == 0:
        inputValues.append(i)
a, n = inputValues
sum = 0
for i in range(n):
    sum += a + i
print(sum)