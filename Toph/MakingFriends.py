number = int(input())
div = []
for i in range(1, int(number ** .5) +1):
	if number % i == 0:
		if number // i == i:
			div.append(i)
		else:
			div.extend([i, number//i])
print(len(div) - 1)