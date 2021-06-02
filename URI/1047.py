gameHour = lambda x,  y: y - x if y > x else 24 + y - x
gameMinute = lambda xm, ym: (1, 60 + ym - xm) if ym < xm else ((0, ym - xm) if ym > xm else (0, xm - ym))
ah, am, bh, bm = map(int, input().split())
gHour = gameHour(ah , bh)
aMinute, bMinute = gameMinute(am, bm)
if gHour == 24 and aMinute == False:
    if gHour > 23 and bMinute > 0:
        gHour = 0
        print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (gHour, bMinute))
    else:
        print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (gHour, bMinute))
elif aMinute == True:
    gHour -= 1
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (gHour, bMinute))
else:
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (gHour, bMinute))