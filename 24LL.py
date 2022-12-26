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
            
    def get(self, idx):
        n = self.head
        count = 0
        while n != None:
            if count == idx:
                return n.element
            n = n.next
            count += 1
        

a1 = [10, 20, 30, 40]
h1 = LinkedList(a1)
val = h1.get(2)
print(val)