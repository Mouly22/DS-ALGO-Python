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
            
    def forwardprint(self):
        n = self.head.next
        while n.element != None:
            print(n.element, end =' ')
            n = n.next
            if n.element == None:
                break
        print()
    
    def backwardprint(self):
        n = self.head.prev
        while n.element != None:
            print(n.element, end = ' ')
            n = n.prev
            if n.element == None:
                break
        print()
        
    
    def remove(self,idx):
        c_n = self.head.next
        c_count = 0
        while c_n.element != None:
            c_count += 1
            c_n = c_n.next
            if c_n.element == None:
                break
        store = c_count
            
        n = self.head.next
        temp = n.next
        count = 1
        rtn = None
        if idx < 0 or idx > store:
            rtn = 'None'
            
        elif idx == 0:
            rtn = self.head.next.element
            self.head.next = n.next
            temp.prev = self.head
           
        else:
            ex = n
            crnt = n.next
            nxt = temp.next
            while crnt.element != None:
                rtn = crnt.element
                if count == idx:
                    ex.next = crnt.next
                    nxt.prev = ex
                    break
                
                ex = ex.next
                crnt = crnt.next
                nxt = nxt.next
                count += 1
        return str(rtn)
        


a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70. 
h3.backwardprint()
# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.  
h3.backwardprint() # This should print: 70,60,50,40,30,20.  
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.  
h3.backwardprint() # This should print: 70,60,40,30,20.  
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60. 
h3.backwardprint() # This should print: 60,40,30,20.