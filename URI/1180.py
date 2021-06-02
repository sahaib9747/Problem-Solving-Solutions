tCase = int(input())
array = list(map(int, input().split()))

print("Menor valor: %i\nPosicao: %i" % (min(array), array.index(min(array))))
