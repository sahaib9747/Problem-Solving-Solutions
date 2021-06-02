import sys


def main():
    data = [float(sys.stdin.readline().strip()) for i in range(100)]
    for i, j in enumerate(data):
        if j <= 10:
            print("A[%i] = %.1f" % (i, j))


if __name__ == '__main__':
    main()