numbers = "0123456789"

userNumber = input()

result = []

for i in range(10):
    result.append(userNumber.count(numbers[i]))

print(result.index(max(result)))
