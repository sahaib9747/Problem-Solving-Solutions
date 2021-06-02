distance = lambda x1, y1 , x2 , y2: ( (x2 - x1) ** 2 + (y2 - y1) ** 2 ) **.5
if __name__ == '__main__':
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    print("%.4f" % distance(x1, y1, x2, y2))