# returns the index of the Node containing the given element.
  # if the element does not exist in the List, return -1.
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
                
    def indexOf(self, elem):
        n = self.head
        count = 0
        while n != None:
            if n.element == elem:
                return count
            n = n.next
            count +=1
        return -1
        

a1 = [10, 20, 30, 40]
h1 = LinkedList(a1) 
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that doesn't exists in the list this will print -1.