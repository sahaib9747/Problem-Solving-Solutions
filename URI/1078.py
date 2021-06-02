def recursion(n ,sum = 0, counter = 1):
    sum += n
    print("%i x %i = %i" %(counter , n , sum))
    if counter == 10:
        return None
    counter += 1
    recursion(n,sum,counter)
n = int(input())
recursion(n)