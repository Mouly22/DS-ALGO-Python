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



    def contains(self, elem):
        n = self.head
        while n != None:
            if n.element == elem:
                return True
            n = n.next
        return False
    
    

# returns true if the element exists in the List, return false otherwise.
a1 = [10, 20, 30, 40]
h1 = LinkedList(a1) 
ask = h1.contains(40)
print(ask) # This should print: True.