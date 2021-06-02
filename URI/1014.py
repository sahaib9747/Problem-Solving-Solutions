avConsumption = lambda km, lt: km / lt
def main():
    print("%.3f km/l" % avConsumption(int(input()), float(input())))
    return None
main()