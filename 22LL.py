class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n


#  Design the constructor based on data type of a. If 'a' is built in python list then
  #  Creates a linked list using the values from the given array. head will refer to the Node that contains the element from a[0]
  #  Else Sets the value of head. head will refer to the given LinkedList

  # Hint: Use the type() function to determine the data type of a
class LinkedList:
    def __init__(self, a):
        if type(a) == list:
            self.head = Node(a[0], None)
            n = self.head
            for elm in range(1, len(a)):
                val = Node(a[elm], None)
                n.next = val
                n = val
        else:
            self.head = a
            
    def countNode(self):
        n = self.head
        count = 0
        while n != None:
            count += 1
            n = n.next
        return count
    
    def printList(self):
        n = self.head
        while n != None:
            if n.next == None:
                print(n.element, end= '')
            else:
                print(n.element, end = ', ')
            n = n.next
        print()
            
        
a1 = [10, 20, 30, 40]
h1 = LinkedList(a1) # Creates a linked list using the values from the array
# head will refer to the Node that contains the element from a[0]

h1.printList() # This should print: 10,20,30,40
print(h1.countNode()) # This should print: 4