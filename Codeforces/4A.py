inp = int(input())
 
res = inp / 2
 
if res % 2 == 0 or (res + 1) % 2 == 0:
    if inp == 2:
        print('NO')
    else:
        print('YES')
 
else:
    print('No')