arr = [int(input()) for i in range(5)]
evenChecker = (lambda array: [1 for i in arr if i % 2 == 0])(arr)
negChecker = (lambda array: [1 for i in arr if i < 0])(arr)
zero = 0

if 0 in arr:
    zero = arr.count(0)

print("%i valor(es) par(es)\n%i valor(es) impar(es)\n%i valor(es) positivo(s)\n%i valor(es) negativo(s)" % (len(evenChecker),5 - len(evenChecker),5 - len(negChecker) - zero,len(negChecker)))