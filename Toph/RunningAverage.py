testCase = int(input())
preNum = 0
userData = list(map(int, input().split()))
for i in range(1, testCase+1):
	preNum += userData[i - 1]
	print(preNum / i) 
	
	