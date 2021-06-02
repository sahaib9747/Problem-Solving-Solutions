userInput = [int(input()) for i in range(100)]
print("%i\n%i" % (max(userInput), userInput.index(max(userInput)) + 1))