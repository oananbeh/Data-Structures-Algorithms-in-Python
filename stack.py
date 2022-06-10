class ArrayStack:
    def __init__ (self):
        self.data = []
    def len (self): 
        return len(self.data)
    def isempty(self):
        return len(self.data) == 0
    def push(self, e):
        self.data.append(e) 
    def top(self):
        if self.isempty():
            print('Stack is Empty' ) 
        return self.data[-1]
    def pop(self):
        if self.isempty():
            print( 'Stack is Empty' )
        return self.data.pop()


newStack=ArrayStack()
print(newStack.isempty())
newStack.push(1)
newStack.push(2)
newStack.push(3)
newStack.push(4)
newStack.push(5)
print(newStack.top())
newStack.pop()
print(newStack.top())
newStack.pop()
print(newStack.top())