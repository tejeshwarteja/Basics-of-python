class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == 0
    
    def push(self, item):   
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")
        
    def size(self):
        return len(self.items)
    
stack= Stack()
print("is the stack empty:", stack.is_empty())
stack.push(1)
stack.push(2)0
stack.push(3)
print("stack:",stack.items)
print("top:",stack.peek())
print("pop",stack.pop())
print("stack after pop", stack.items)
print("is the stack empty", stack.is_empty())
print("size of the stack", stack.size())
