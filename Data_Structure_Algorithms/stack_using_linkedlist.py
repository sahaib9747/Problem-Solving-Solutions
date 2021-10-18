"""
Stack using LinkedList
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.head = Node()
        self.numberOfElements = 0
    
    def push(self, data):
        """if node doesn't exist, it will just create e node and  link to the head node
        but if any node is exists then it will search from 1st node to most recent node
        """
        if not self.numberOfElements:
            self.head.next = Node(data)  # pointer of first node
        else:
            presentNode = self.head.next 
            while presentNode.next:
                presentNode = presentNode.next  # most recent node
            
            presentNode.next = Node(data)  # new node will be store in the head of stuck

        self.numberOfElements += 1



    def pop(self):
        """ This method will return the head value of stack.
            if numberOfElements in stack is 1, then the head.next will None, 
            That's why we are also storing the head node in the nodes list.

            we can implements without storing head node, but redanded code need to be written.
            if any node is exist then it will search for most recent node from head node.
        """
        if not self.numberOfElements:
            return "No data is available, Stuck is Empty"
        else:
            presentNode = self.head
            nodes = [presentNode]
            while presentNode.next:
                presentNode = presentNode.next # most recent node
                nodes.append(presentNode)  # all of nodes will be store

            temp = presentNode.data
            nodes[-2].next = None 
            self.numberOfElements -= 1
            return temp

    def top(self):
        if not self.numberOfElements:
            return "No data is available, Stuck is Empty"
        else:
            presentNode = self.head.next

            while presentNode.next:
                presentNode = presentNode.next 

            return presentNode.data 

    def size(self):
        return self.numberOfElements

    
        
obj = Stack()

obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)

print(obj.numberOfElements)

print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.numberOfElements)
print(obj.pop())
print(obj.pop())

print(obj.size())

print(obj.top())
