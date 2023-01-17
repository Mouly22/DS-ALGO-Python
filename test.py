class Stack_string():
    def __init__(self, val, idx):
        self.value = val
        self.index = idx

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
            self.counter -= 1
        return value
    
    def isEmpty(self):
        if self.counter == 0:
            return True
        return False
        
a1 = ArrayStack(20)
c_store = 0 
v_store = None
inp = input(f'Enter Input:' )
#inp = '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
flag = True
var = None
res = None
for i in range(len(inp)):
    b1 = Stack_string(inp[i], i)
    if inp[i] == '(' or inp[i] == '{' or inp[i] == '[':
        a1.push(b1)
   
    elif inp[i] == ')' or inp[i] == '}' or inp[i] == ']':
        if a1.isEmpty() == True:
            var = b1
            c_store = b1.index
            v_store = b1.value 
            flag = False
            break
        else:
            var = a1.pop()
            if inp[i] == ')':
                if var.value == '(':
                    pass
                elif var.value != '(':
                    flag = False
                    v_store = var.value
                    c_store = var.index

                    break
            elif inp[i] == '}':
                if var.value == '{':
                    pass
                elif var.value != '{':
                    flag = False
                    v_store = var.value
                    c_store = var.index
                    break
            elif inp[i] == ']':
                if var.value == '[':
                    pass
                elif var.value != '[':
                    flag = False
                    v_store = var.value
                    c_store = var.index
                    break

if a1.isEmpty() != True:
    flag = False 
    
if var == None:
    var = Stack_string(inp[i], i)
    print(var.value)       
        
if flag:
    print('This expression is correct.')
else:
    if a1.isEmpty() == True:
        print(f"This expression is NOT correct.\nError at character #{c_store}. '{v_store}'- not opened.")
    elif a1.isEmpty() != True:
        var2 = a1.pop()
        print(f"This expression is NOT correct.\nError at character #{var.index}. '{var.value}'- not closed.")
    else:
        print(f"This expression is NOT correct.\nError at character #{c_store}. '{v_store}'- not closed.")