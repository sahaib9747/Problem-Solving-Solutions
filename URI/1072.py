checker = lambda x: 10 <= x <= 20
intervalIn = 0
interValOut = 0
tcase = int(input())

for i in range(tcase):
    userInput = int(input())
    if checker(userInput) == True:
        intervalIn += 1
    else:
        interValOut += 1
        
print("%i in\n%i out" % (intervalIn, interValOut))