class Stack:
    def __init__(self, stack_size):
        self.size = stack_size
        self.db = [False] * self.size
        self.top = -1

    def push(self, item):
        if len(self.db) <= self.size-1:
            self.top += 1
            self.db[self.top] = item
            print(item)
            return True
        else:
            return 'Stack Overflow'

    def pop(self):
        if self.db:
            data = self.db[self.top]
            self.db[self.top] = False
            self.top -= 1
            return data

        return 'Stack Underflow'


    def top(self):
        return self.db[self.top]

    def __str__(self):
        return str(self.db)
    
my_stack = Stack(10)

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
print(my_stack)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
