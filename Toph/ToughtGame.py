tCase = int(input())
while tCase:
    fNum, sNum = map(int, input().split())
    print("Sadia will be happy." if ((fNum + sNum) // 2) % 2 == 0 else "Oops!")
    tCase -= 1