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
            return 'Stack Underflow!'
        else:
            return self.head.element
            
    def pop(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp.element
    
b1 = LLStack()
print(f'Push {b1.push(10)}')
print(f'Push {b1.push(30)}')
print(f'Push {b1.push(50)}')
print(f'Push {b1.push(100)}')
print(f'Pop {b1.pop()}')
print(f'Peek {b1.peek()}')
print(f'Push {b1.push(20)}')
print(f'Pop {b1.pop()}')
print(f'Pop {b1.pop()}')
print(f'Peek {b1.peek()}') 