class Stack:
    def __init__(self, data):
        self.data = data
        self.items = [False] * len(self.data)

    def push(self, index=0):
        if len(self.data) == index:
            return
        self.items[index] = self.data[index]
        index += 1
        return self.push(index)

    def pop(self, revVal=""):
        if self.isEmpty():
            if revVal == self.data:
                return "Yes"
            return "No"
        revVal += self.items.pop()
        return self.pop(revVal)

    def isEmpty(self):
        if self.items == []:
            return True
        return False

def main():
    stack = Stack(input())
    stack.push()
    print(stack.pop())


if __name__ == "__main__":
    main()



