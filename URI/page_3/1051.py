salary = float(input())
percent = [8, 18, 28]
taxes = 0
if salary > 2000:
    salary -= 2000
    for i in range(3):
        if salary > 0:
            money = [1000, 1500, salary]
            if salary >= money[i]:
                taxes += money[i] / 100 * percent[i]
                salary -= money[i]
            else:
                taxes += salary / 100 * percent[i]
                break
        else:
            break
    print("R$ %.2f" % taxes)
else:
    print("Isento")