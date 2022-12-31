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
                print(n.element, end=', ')
            n = n.next
        print()
        
    def copyList(self):
        l_head = Node(10, None)
        v = self.head
        store = l_head
        while v.next != None:
            val2 = Node(v.next.element, None)
            store.next = val2
            store = val2
            v = v.next
        return l_head
            


        
print("////// Test 07 //////")
a2 = [10,20,30,40,50,60,70]
h2 = LinkedList(a2) # uses theconstructor where a is an built in list
h2.printList() # This should print: 10,20,30,40,50,60,70.  
# Makes a duplicate copy of the given List. Returns the head reference of the duplicate list.
copyH = h2.copyList() # Head node reference of the duplicate list
h3 = LinkedList(copyH) # uses the constructor where a is head of a linkedlist 
h3.printList() # This should print: 10,20,30,40,50,60,70.  