def maiorAb(x, y , z = 0):
    greatest = (x + y + abs(x - y)) // 2
    if z != 0:
        return maiorAb(greatest , z)
    return greatest
def main():
    a, b, c = map(int , input().split())
    print("%i eh o maior" % maiorAb(a, b , c))
main()