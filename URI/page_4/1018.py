msg = ["nota(s) de R$ 100,00", "nota(s) de R$ 50,00", "nota(s) de R$ 20,00", "nota(s) de R$ 10,00",
       "nota(s) de R$ 5,00", "nota(s) de R$ 2,00", "nota(s) de R$ 1,00"]
notes = [100, 50, 20, 10, 5, 2, 1]
counting = lambda money, note: (money % note, money / note)
money = int(input())
print(money)
for i in range(7):
    money, note = counting(money, notes[i])
    print("%i %s" % (note, msg[i]))