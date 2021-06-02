def loop(n):
    if n > 100:
        return 0
    else:
        print(n)
        n += 2
    loop(n)
    
loop(2)