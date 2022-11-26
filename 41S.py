#stack palindrome check
class Help:
    def __init__(self, value, idx):
        self.value = value
        self.index = idx

class ArrayStack():
    def __init__(self, size):
        self.size = size
        self.counter = 0
        self.sarray = [None]*size
        
    def push(self, val):
        if self.counter >= self.size:
            print('Stack overflow')
        else:
            self.sarray[self.counter] = val
            self.counter += 1
        return self.sarray
    
    def peek(self):
        if self.size == 0:
            print('Stack underflow')
        else:
            print(self.sarray[self.counter - 1]) 
        
    def pop(self):
        if self.size == 0:
            return None
        else:
            value = self.sarray[self.counter- 1]
            self.sarray[self.counter - 1] = None
            self.counter -= 1
        return value
    
    def isEmpty(self):
        if self.counter == 0:
            return True
        return False
p1 = ArrayStack(10)
inp = 'nursesrun'
for i in range(len(inp)):
    q1 = Help(inp[i], i)
    p1.push(q1)
    #print(q1.value)
for j in range(i+1):
    val2 = p1.pop()
    #print(val2.value)
    

if q1.value == val2.value:
    print(True)
else:
    print(False)