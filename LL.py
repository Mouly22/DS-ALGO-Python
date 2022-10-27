class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(Node):
    def __init__(self):
        self.head = None

    def traverse(self, data):
        super().__init__(data = data)
        if self.head == None:
            print('Linked list is empty')
        else:
            n = self.head
            while n != None:
                print(self.data)
            n = self.next

a = Node(10)
b = LinkedList()
b.traverse(10)




