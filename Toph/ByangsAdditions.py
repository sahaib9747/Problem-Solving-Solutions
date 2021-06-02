a, b = input().split()
carry = False
a = list(map(int, a))
b = list(map(int, b))
minLen = min(len(a), len(b))

for i in range(minLen):
	if a.pop() + b.pop() > 9:
		carry = True
		break
if carry:
	print("Yes")
else:
	print("No")
