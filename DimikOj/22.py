# sieve of eratosthenes
def prime(end):

    numbers = list(range(3, end+1, 2))
    for i in range(len(numbers)):
        if numbers[i]:
            for j in range(numbers[i] + i, len(numbers), numbers[i]):
                numbers[j] = False
            numbers[i] = True
    return numbers.count(True)

tcase = int(input())

for case in range(tcase):
    start, end = map(int, input().split())
    totalPrime = prime(end) - prime(start)
    if start > 2:
        print(totalPrime)
    else:
        print(totalPrime+1)