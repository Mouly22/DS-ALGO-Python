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
        else:
            self.head = a
            
    def printList(self):
        n = self.head
        while n != None:
            if n.next == None:
                print(n.element, end = '')
            else:
                print(n.element, end = ', ')
            n = n.next
        print()


    def rotateLeft(self):
        n = self.head
        store = self.head.element
        while n.next != None:
            n.element = n.next.element
            n = n.next
            if n.next == None:
                n.element = store
    
    
print("////// Test 11 //////")
a8 = [10,20,30,40]
h8 = LinkedList(a8) # uses theconstructor where a is an built in list
h8.printList() # This should print: 10,20,30,40.  
    
# Rotates the list to the left by 1 position.
h8.rotateLeft()
h8.printList() # This should print: 20,30,40,10.