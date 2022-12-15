# removes Node at the given index. returns element of the removed node.
  # Check validity of index. return None if index is invalid.
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
                print(n.element, end = ', ')
            n = n.next
        print()

    def remove(self, idx):
        imp = self.head
        counts = 1
        blank = None
        flag = True
        rtn = None
        if idx == 0:
            rtn = self.head.element
            blank = self.head
            self.head = self.head.next
            flag = False
        else:
            cu = imp.next
            ex = imp
            while cu != None:
                if counts == idx:
                    rtn = cu.element
                    ex.next = cu.next
                    break
                cu = cu.next
                ex = ex.next
                
                counts += 1
                flag = False
        return rtn
        if flag:
            print('Index Error')
   
    
print("////// Test 10 //////")
a7 = [10,20,30,40,50,60,70]
h7 = LinkedList(a7) # uses theconstructor where a is an built in list
h7.printList() # This should print: 10,20,30,40,50,60,70.  
    
# removes Node at the given index. returns element of the removed node.
# Check validity of index. return None if index is invalid.
    
print("Removed element:",h7.remove(0)) # This should print: Removed element: 10
h7.printList() # This should print: 20,30,40,50,60,70.  
print("Removed element: ",h7.remove(3)) # This should print: Removed element: 50
h7.printList() # This should print: 20,30,40,60,70.  
print("Removed element: ",h7.remove(4)) # This should print: Removed element: 70
h7.printList() # This should print: 20,30,40,60. 