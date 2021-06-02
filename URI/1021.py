msg = [
        "nota(s) de R$ 100.00", "nota(s) de R$ 50.00", "nota(s) de R$ 20.00", "nota(s) de R$ 10.00",
       "nota(s) de R$ 5.00", "nota(s) de R$ 2.00", "moeda(s) de R$ 1.00", "moeda(s) de R$ 0.50",
       "moeda(s) de R$ 0.25", "moeda(s) de R$ 0.10", "moeda(s) de R$ 0.05", "moeda(s) de R$ 0.01"
      ]
notes = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
counting = lambda money, note: (money % note, money / note)

if __name__ == '__main__':
    money = float(input())
    for i in range(12):
        if i == 0:
            print("NOTAS:")
        elif i == 6:
            print("MOEDAS:")
        money, note = counting(money, notes[i])
        money = float(format(money, '.2f'))
        print("%i %s" % (note, msg[i]))