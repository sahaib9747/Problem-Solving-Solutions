value = {}
def fac(n):
    if n in value:
        return value[n]
    if n == 0:
        return 1
    else:
        facto = n * fac(n - 1)
        value[n] = facto
    return facto
print(fac(int(input())))