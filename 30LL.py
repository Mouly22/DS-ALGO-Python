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
            
                    
       
        
# inserts Node containing the given element at the given index
#   Check validity of index.
    def insert(self, elem, idx):
        strt = self.head
        count1 = 0
        node = Node(elem, None)
        flag = True
        
        if idx == 0:
            node.next = self.head
            self.head = node
            flag = False

        else:
            while strt != None:
                if count1 == idx - 1:
                    node.next = strt.next
                    strt.next = node
                    flag = False
                strt = strt.next
                count1 += 1
        if flag:
            print('Index Error')                 
            
        
print("////// Test 09 //////")
a6 = [10,20,30,40]
h6 = LinkedList(a6) # uses theconstructor where a is an built in list
h6.printList() # This should print: 10,20,30,40.  
# inserts Node containing the given element at the given index. Check validity of index.
h6.insert(85,0)
h6.printList() # This should print: 85,10,20,30,40.  
h6.insert(95,3)   
h6.printList() # This should print: 85,10,20,95,30,40.  
h6.insert(75,6)
h6.printList() # This should print: 85,10,20,95,30,40,75. 