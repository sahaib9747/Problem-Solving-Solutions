display = ["NULL", "EVEN POSITIVE", "EVEN NEGATIVE", "ODD POSITIVE", "ODD NEGATIVE"]
evenOdd = lambda n: [n == 0, n % 2 == 0 and n > 0, n % 2 == 0 and n < 0, n % 2 != 0 and n > 0, n % 2 != 0 and n < 0]

tCase = int(input())
output = [int(input()) for i in range(tCase)]
for userInput in output:
    conChecker = evenOdd(userInput)
    print(display[conChecker.index(True)])