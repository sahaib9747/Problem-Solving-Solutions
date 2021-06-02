def sequence(x = 1,n = 1):
    if n == 101:
        return 0
    Sum = x / n
    n += 1
    #this line will call function,it self.
    return Sum + sequence(x,n)
print("%.2f" % sequence())