animals = [False] * 3  # [0] = C, [1] = R , [2] = S
tCase = int(input())
indexChooser = lambda a: (0, int(a[0])) if 'C' in a else((1, int(a[0])) if 'R' in a else (2, int(a[0])))
percentConverter = lambda n, animal: n * 100 / sum(animal)

for i in range(tCase):
    tempArray = input().split(' ')
    index, amount = indexChooser(tempArray)
    animals[index] += amount

display = ["Total: %i cobaias" % sum(animals),
           "Total de coelhos: %i" % animals[0],
           "Total de ratos: %i" % animals[1],
           "Total de sapos: %i" % animals[2],
           "Percentual de coelhos: %.2f %s" % (percentConverter(animals[0], animals), '%'),
            "Percentual de ratos: %.2f %s" % (percentConverter(animals[1], animals), '%'),
            "Percentual de sapos: %.2f %s" % (percentConverter(animals[2], animals), '%'),
           ]
           
for out in display:
    print(out)