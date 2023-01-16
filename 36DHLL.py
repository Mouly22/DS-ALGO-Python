class Node:
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p

class DoublyList:
    def __init__(self,a):
        if type(a) == list:
            self.head = Node(None, None, None)
            n = self.head
            flag = True
            for i in range(0, len(a)):
                val = Node(a[i], None, None)
                n.next = val
                val.prev = n
                n = val
            n.next = self.head
            self.head.prev = n   

    # returns the index of the containing the given element. if the element does not exist in the List, return -1.
    def indexOf(self, elem):
        n = self.head.next
        count = 0
        while n.element != None:
            if n.element == elem:
                return count
            count += 1
            n = n.next
        return -1


a1 = [10, 20, 30, 40]
h1 = DoublyList(a1)
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that 
#doesn't exists in the list this will print -1.