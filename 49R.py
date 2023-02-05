#Implement a recursive algorithm to add all the elements of a non-dummy headed singly linked linear list. Only head of the list will be given as parameter where you may assume every node can contain only integer as its element.
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

def summ(n_head):
    if n_head == None:
        return 0
    else:
        return n_head.element + summ(n_head.next)

array = [10, 20, 40, 90, 50]
a1 = LinkedList(array)
print(summ(a1.head))