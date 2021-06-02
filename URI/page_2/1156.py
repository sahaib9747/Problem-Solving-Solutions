def sequence(x = 1,n = 1):
    if x > 39:
        return 0
    elif x == 1:
        Sum = 1
        x, n = 3, 2 
    else:
        Sum = x / n
        x += 2
        n *= 2
    #this line will call function,it self.
    return Sum + sequence(x,n)
print("%.2f" % sequence())