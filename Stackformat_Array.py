class ArrayStack():
    def __init__(self, size):
        self.size = size
        self.counter = 0
        self.sarray = [None]*size
        
    def push(self, val):
        if self.counter >= self.size:
            return 'Stack overflow'
        else:
            self.sarray[self.counter] = val
            self.counter += 1
        return self.sarray
    
    def peek(self):
        if self.size == 0:
            print('Stack underflow')
        else:
            return self.sarray[self.counter - 1] 
        
    def pop(self):
        if self.size == 0:
            return None
        else:
            value = self.sarray[self.counter- 1]
            self.sarray[self.counter - 1] = None
            #self.sarray = self.sarray[:-1]
            self.counter -= 1
        return value
    
    def isEmpty(self):
        if self.counter == 0:
            return True
        return False        
        
        
a1 = ArrayStack(10)
a1.push(20)
print(a1.push(40))
a1.peek()
print(a1.pop())
print(a1.sarray)