class Node:
    def __init__(self, data = None, dnext = None):
        self.data = data
        self.dnext = dnext
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    
    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        val = self.head
        lval = ''
        
        while val:
            lval += str(val.data) + '-->'
            val = val.dnext
            
        print(lval)
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        val = self.head
        
        while val.dnext:
            val = val.dnext
        
        val.dnext = Node(data, None)
        
    def insert_values(self, data_list):
        #self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        count = 0
        val = self.head
        while val:
            count += 1
            val = val.dnext
        return count
            
        
    def remove_at(self, index):
        if index < 0 and index>= self.get_length():
            raise Exception
        if index == 0:
            self.head = self.head.dnext
            return
        
        count = 0
        val = self.head
        while val:
            if count == index - 1:
                val.dnext = val.dnext.dnext
                break
            val = val.dnext
            count += 1
            
    def insert_at(self, index, data):
        if index < 0 and index >= self.get_length():
            raise Exception('Invalid Syntax')
            
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        val = self.head
        while val:
            if count == index - 1:
                node = Node(data, val.dnext)
                val.dnext = node
                break
            val = val.dnext
            count += 1
        
    
        
if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_beginning(5)
    l1.insert_at_beginning(95)
    l1.insert_at_end(65)
    l1.insert_at_end(59)
    l1.insert_values(['mouly', 'loves','cookies'])
    l1.get_length()
    l1.remove_at(3)
    l1.insert_at(1, 'Street')
    l1.insert_at(5, 'smol catto')
    l1.print()
            