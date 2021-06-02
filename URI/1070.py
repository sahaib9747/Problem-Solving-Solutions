counter = 1
user = int(input())
while True:
    if user % 2 == 0:
        user += 1
    print(user)
    user += 2
    if counter == 6:
        break
    counter += 1