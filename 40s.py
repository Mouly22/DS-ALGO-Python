# Output 1
# 1+2*(3/4)
# This expression is correct.
 
# Output 2
# 1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14
# This expression is NOT correct.
# Error at character # 10. ‘{‘- not closed.
 
# Output 3
# 1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14
# This expression is correct.

# Output 4
# 1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14
# This expression is NOT correct.
# Error at character # 4. ‘]‘- not opened.

class Stack_string():
    def __init__(self, val, idx):
        self.value = val
        self.index = idx

class Node:
    def __init__(self, elem, nxt):
        self.element = elem
        self.next = nxt
        
class LLStack:
    def __init__(self):
        self.head = None
        
    def push(self, val):
        node = Node(val, self.head)
        self.head = node
        return node.element
    
    def peek(self):
        if self.head == None:
            print('Stack Underflow!')
        else:
            print(self.head.element)
            
    def pop(self):
        n = self.head
        self.head = self.head.next
        n.next = None
        return n.element

    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
c1 = LLStack()
c_store = 0 
v_store = None
#inp = input(f'Enter Input:' )
inp = '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
flag = True
res = None
for i in range(len(inp)):
    d1 = Stack_string(inp[i], i)
    if inp[i] == '(' or inp[i] == '{' or inp[i] == '[':
        c1.push(d1)
   
    elif inp[i] == ')' or inp[i] == '}' or inp[i] == ']':
        if c1.isEmpty() == True:
            var = d1
            c_store = d1.index
            v_store = d1.value 
            flag = False
            break
        else:
            var = c1.pop()
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


if c1.isEmpty() != True and flag== True:
    var2 = c1.pop()
    v_store = var2.value
    c_store = var2.index
    flag = False 
    
if var == None:
    var = Stack_string(inp[i], i)
    print(var.value)
          
        
if flag:
    print('This expression is correct.')
else:
    if var.value == '(' or var.value == '{' or var.value == '[':
        res = 'closed'
    else:
        res = 'opened'
            
    if c1.isEmpty() == True:
        print(f"This expression is NOT correct.\nError at character #{c_store+1}. '{v_store}'- not {res}.")
    elif c1.isEmpty() != True:
        print(f"This expression is NOT correct.\nError at character #{var.index+1}. '{var.value}'- not {res}.")
    else:
        print(f"This expression is NOT correct.\nError at character #{c_store+1}. '{v_store}'- not {res}.")
