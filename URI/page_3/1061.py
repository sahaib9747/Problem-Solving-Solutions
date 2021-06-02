startDay, startTime, endDay, endTime = ''.join(input().split('Dia ')), input().split(' : '), ''.join(input().split('Dia ')), input().split(' : ')
startDay = int(startDay)
endDay = int(endDay)
startHour, startMinute, startSecond = int(startTime[0]), int(startTime[1]), int(startTime[2])
endHour, endMinute, endSecond = int(endTime[0]), int(endTime[1]), int(endTime[2])

dayCal = (lambda x, y: y - x)(startDay, endDay)
carryHour, hourCal = (lambda a, b: (0, b - a) if b > a else ((1, b + 24 - a) if a > b else (0, a - b)))(startHour, endHour)
carryMinute, minuteCal = (lambda a, b: (0, b - a) if b > a else ((1, b + 60 - a) if a > b else (0, a - b)))(startMinute, endMinute)
carrySec, secondCal = (lambda a, b: (0, b - a) if b > a else ((1, b + 60 - a) if a > b else (0, a - b)))(startSecond, endSecond)

if carrySec == 1 and minuteCal > 0:
    minuteCal -= 1
if carryMinute == 1 and hourCal > 0:
    hourCal -= 1
if carrySec == 1 and minuteCal == 0 and hourCal > 0:
    hourCal -= 1
    minuteCal = 59
if carryHour == 1 and dayCal > 0:
    dayCal -= 1
print("%i dia(s)\n%i hora(s)\n%i minuto(s)\n%i segundo(s)" % (dayCal, hourCal, minuteCal, secondCal))