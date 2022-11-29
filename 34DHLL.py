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
            
                
        else:
            self.head = a
        
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
        
                
           
    def countNode(self):
        count = 0 
        n = self.head.next
        while n.element != None:
            count += 1
            n = n.next
        return count
        
  
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array

h1.forwardprint() # This should print: 10,20,30,40. 
h1.backwardprint() # This should print: 40,30,20,10. 
print(h1.countNode()) # This should print: 4