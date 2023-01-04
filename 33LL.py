class Node:
    def __init__(self,e, n):
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
            print(n.element, end = ' ')
            n = n.next
        print()


    def rotateRight(self):
        n = self.head
        count = 0
        while n != None:
            count += 1
            n = n.next
        store = count
        val1 = self.head.element
        val2 = self.head.next
        for i in range(1, count):
            var = val2.element
            val2.element = val1
            val1 = var
            val2 = val2.next
        self.head.element = var  
              
    
print("////// Test 12 //////")
a9 = [10,20,30,40]
h9 = LinkedList(a9) # uses theconstructor where a is an built in list
h9.printList() # This should print: 10,20,30,40.  
    
# Rotates the list to the right by 1 position.
h9.rotateRight()
h9.printList() # This should print: 40,10,20,30.