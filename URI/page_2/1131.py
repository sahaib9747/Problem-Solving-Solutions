winChecker = lambda i, g: "Inter venceu mais" if i > g else (("Gremio venceu mais") if g > i else "Não houve vencedor")
conCheck = lambda a, b, c, d, e, f: (a + 1, b, c, f + 1) if d > e else ((a, b + 1, c, f + 1) if e > d else (a, b, c + 1, f + 1))
interWon, gremioWon, matchDraw, totalMatch = 0, 0, 0, 0
display = []

while True:
    x, y = map(int, input().split())
    interWon, gremioWon, matchDraw, totalMatch = conCheck(interWon, gremioWon, matchDraw, x, y, totalMatch)
    display.append("Novo grenal (1-sim 2-nao)")
    repeat = int(input())
    if repeat == 1:
        continue
    else:
        break
    
display.extend(["%i grenais" % totalMatch, "Inter:%i" % interWon, "Gremio:%i" % gremioWon, "Empates:%i" % matchDraw, winChecker(interWon, gremioWon)])
print(*display, sep="\n")