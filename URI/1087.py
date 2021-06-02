import sys


def chess():
    """This function will print out the needed moves to go the proper destination of queen."""
    row1, col1, row2, col2 = map(int, sys.stdin.readline().strip().split())
    if not row1:  # if anyone is false, then break the loop.
        return 0
    elif row1 == row2 and col1 == col2:  # if present position and destination is same then move is 0
        print(0)
    # if row == row or col == col or diagonally distance is same then 1 move needed
    elif row1 == row2 or col1 == col2 or abs(row2 - row1) == abs(col2 - col1):
        print(1)
    else:
        print(2)  # if all of con are false. so its needed highest 2 moves.
    return chess()


def main():
    chess()


if __name__ == '__main__':
    sys.setrecursionlimit(9999)
    main()
