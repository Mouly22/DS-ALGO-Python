# updates the element of the Node at the given index. 
  # Returns the old element that was replaced. For invalid index return None.
  # parameter: index, element
class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n
class LinkedList:
    def __init__(self, a):
        if type(a) == list:
            self.head = Node(a[0], None)
            n = self.head
            for i in range(1, len(a)):
                val = Node(a[i], None)
                n.next = val
                n = val
                
    def printList(self):
        n = self.head
        while n != None:
            if n.next == None:
                print(n.element, end = '')
            else:
                print(n.element, end=', ')
            n = n.next
        print()
        
                
    def set(self, idx, elem):
        n = self.head
        a = None
        count = 0
        while n != None:
            if count == idx:
                a = n.element
                n.element = elem
            n = n.next
            count += 1
        return a
            
            
    
a1 = [10, 20, 30, 40]
h1 = LinkedList(a1)       
print(h1.set(1,85)) # This should print: 20
h1.printList() # This should print: 10,85,30,40.
print(h1.set(15,85)) # This should print: None
h1.printList() # This should print: 10,85,30,40. 