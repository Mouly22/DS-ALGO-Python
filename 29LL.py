class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n
class LinkedList:
    def __init__(self, a):
        if type(a) == list:
            self.head = Node(a[0], None)
            modify = self.head
            for i in range(1, len(a)):
                val = Node(a[i], None)
                modify.next = val
                modify = val
        else:
            self.head = a
            
    def printList(self):
        ini = self.head
        while ini != None:
            if ini.next == None:
                print(ini.element, end = '')
            else:
                print(ini.element, end =', ')
            ini = ini.next
        print()

# Makes a reversed copy of the given List. Returns the head reference of the reversed list.
    def reverseList(self):
        n = self.head
        store = 0
        count = 0
        while n != None:
            count +=1
            n= n.next
        store = count
        l_head = Node(None, None)
        v = l_head
        for i in range(store):
            var = self.head
            for j in range(count-i-1):
                var = var.next
            if v.element == None:
                l_head.element = var.element
            else:
                var = Node(var.element, None)
                v.next = var
                v = var
        return l_head


print("////// Test 08 //////")
a4 = [10,20,30,40,50]
h4 = LinkedList(a4) # uses theconstructor where a is an built in list
h4.printList() # This should print: 10,20,30,40,50.  
# Makes a reversed copy of the given List. Returns the head reference of the reversed list.
revH=h4.reverseList() # Head node reference of the reversed list
h5 = LinkedList(revH) # uses the constructor where a is head of a linkedlist 
h5.printList() # This should print: 50,40,30,20,10.