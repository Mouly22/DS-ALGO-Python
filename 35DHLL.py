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
            
    def nodeAt(self, idx):
        n = self.head.next
        count = 0
        while n.element != None:
            
            if count == idx:
                return n
            n = n.next
            count += 1
        
        return Node('index error', None, None)
    


a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(5)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"