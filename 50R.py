#Implement a recursive algorithm which will print all the elements of a non-dummy headed singly linked linear list in reversed order.
class Node:
    def __init__(self, e, nxt):
        self.element = e
        self.next = nxt

class LinkedList:
    def __init__(self, a):
        self.size = len(a)
        self.count = 0
        if type(a) == list:
            self.head = Node(a[0], None)
            n = self.head
            for i in range(1, self.size):
                val = Node(a[i], None)
                n.next = val
                n = val
        else:
            self.head = a
            
def reverse(val):
    if val.next == None:
        print(val.element)
    else:
        reverse(val.next)
        print(val.element)
        
        
        
lst = [50, 40, 30, 90, 0]            
a1 = LinkedList(lst)
reverse(a1.head)