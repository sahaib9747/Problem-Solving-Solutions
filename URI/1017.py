fuelSpent = lambda hour, speed: speed * hour / 12
if __name__ == '__main__':
    print("%.3f" % fuelSpent(int(input()), int(input())))