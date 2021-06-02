arr = [int(input()) for i in range(5)]
conChecker = (lambda array: [1 for i in arr if i % 2 == 0])(arr)
print("%i valores pares" % len(conChecker))