# returns the reference of the Node at the given index. For invalid index return None.
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
                
    def nodeAt(self, idx):
        n = self.head
        count = 0
        while n != None:
            if count == idx:
                return n
            count += 1
            n = n.next
        raise IndexError

    
a1 = [10, 20, 30, 40]
h1 = LinkedList(a1)
# returns the reference of the Node at the given index. For invalid idx return None.
myNode = h1.nodeAt(1)
print(myNode.element) # This should print: 20. In case of invalid index This will generate an Error.