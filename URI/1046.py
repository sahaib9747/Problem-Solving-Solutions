gameTime = lambda x, y: y - x if y > x else 24 + y - x
a, b = map(int, input().split())
if gameTime(a, b):
    print("O JOGO DUROU %i HORA(S)" % gameTime(a, b))
else:
    print("O JOGO DUROU 24 HORA(S)")