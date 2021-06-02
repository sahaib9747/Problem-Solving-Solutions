checker = lambda a, b: "Crescente" if a < b else "Decrescente"
while True:
    x, y = map(int, input().split())
    if x == y:
        break
    else:
        print(checker(x, y))