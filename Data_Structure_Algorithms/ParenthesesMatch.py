# match parentheses using stack

# stack
class Stack:
    def __init__(self, size):
        self.size = size
        self.db = [] 
        self.top = -1

    def push(self, data):
        if self.top < self.size-1:
            self.db.append(data)
            self.top += 1
            print(f"top: {self.top} and size: {self.size}")
        else:
            raise "StackOverFlow"
    
    def pop(self):
        if self.top >= 0:
            data = self.db.pop(-1)
            self.top -= 1
        else:
            raise 'StackUnderFlow'

        return data

    def top(self):
        if self.top >= 0:
            return self.db[-1]

def parentheses_match(lst):
    pass


        


    