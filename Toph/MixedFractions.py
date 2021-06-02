lob, hor = map(int, input().split())

newLob = lob % hor

beforeFractionInt = lob // hor

print("%i %i %i" % (beforeFractionInt, newLob, hor))