tCase = int(input())

for i in range(tCase):
    over = 0
    ball = 0
    userInput = input()
    unCount = ["N", "W", "D"]
    for j in userInput:
        if j in unCount:
            continue
        else:
            ball += 1
    over = ball // 6
    ball = ball % 6
    if over == 1 and ball == 1:
        print("%i OVER %i BALL" % (over, ball))
    elif over == 1 and ball > 1:
        print("%i OVER %i BALLS" % (over, ball))
    elif over > 1 and ball == 1:
        print("%i OVERS %i BALL" % (over, ball))
    elif over > 1 and ball > 1:
        print("%i OVERS %i BALLS" % (over, ball))
    else:
        if over == 0 and ball == 1:
            print("%i BALL" % ball)
        elif over == 1 and ball == 0:
            print("%i OVER" %over)
        elif over > 1 and ball == 0:
            print("%i OVERS" %over)
        else:
            print("%i BALLS" % ball)
