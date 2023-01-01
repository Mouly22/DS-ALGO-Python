class Node:
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p

class DoublyList:
    def __init__(self,a):
        if type(a) == list:
            self.head = Node(None, None, None)
            n = self.head
            flag = True
            for i in range(0, len(a)):
                val = Node(a[i], None, None)
                n.next = val
                val.prev = n
                n = val
            n.next = self.head
            self.head.prev = n
            
    def forwardprint(self):
        n = self.head.next
        while n.element != None:
            print(n.element, end =' ')
            n = n.next
            if n.element == None:
                break
        print()
    
    def backwardprint(self):
        n = self.head.prev
        while n.element != None:
            print(n.element, end = ' ')
            n = n.prev
            if n.element == None:
                break
        print()
        

# inserts containing the given element at the given index Check validity of index. 
    def insert(self, elem, idx):
        n = self.head.next
        node = Node(elem, None, None)
        
        count = 0
        if idx == 0:
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
            n.prev = node
        else:
            while n.element != None:
                temp = n.next
                if count == idx - 1:
                    node.next = temp
                    n.next = node
                    
                    node.prev = n
                    temp.prev = node
                
                n = n.next
                
                count += 1
                if n.element == None:
                    break
                

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40. 
h2.backwardprint()

# # inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40. 
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.  
h2.backwardprint() # This should print: 40,30,95,20,10,80.  

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75. 
h2.backwardprint() # This should print: 75,40,30,95,20,10,85. 