"""
This program will count, how many years after city A populations will be more than city B.
"""


def populationGrowth(PA, PB, GA, GB, years=0):  # recursive method
    if years > 100:
        return "Mais de 1 seculo."
    elif PA > PB:
        return str(years) + ' anos.'
    else:
        PA += int(PA / 100 * GA)
        PB += int(PB / 100 * GB)
        years += 1
        return populationGrowth(PA, PB, GA, GB, years)  # this will return only a value.


tCase = int(input())
display = [False] * tCase
for i in range(tCase):
    PA, PB, GA, GB = map(float, input().split())
    display[i] = populationGrowth(PA, PB, GA, GB)
print(*display, sep="\n")
