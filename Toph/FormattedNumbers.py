class Stack:
    """this is a stack, first in last out"""
    def __init__(self, data):
        self.values = data
        self.items = [False] * len(self.values)  # create locations

    def push(self, value, counter=0):  # it will push all of data from instance values.
        if counter == len(value):
            return self.items
        else:
            self.items[counter] = value[counter]
            counter += 1
        return self.push(value, counter)

    def pop(self, comma=0, newNumber=""):  # it will pop all data with comma with reversed order
        if self.isEmpty():
            return newNumber
        elif comma == 3:
            newNumber += ","
            comma = 0
        newNumber += self.items.pop()
        comma += 1
        return self.pop(comma, newNumber)

    def isEmpty(self):
        if self.items == []:
            return True
        return False


def main():
    stack = Stack(input())
    stack.push(stack.values)
    fNumber = stack.pop()
    print(fNumber[::-1])


if __name__ == "__main__":
    main()
