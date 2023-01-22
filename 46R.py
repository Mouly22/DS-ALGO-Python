#Print all the elements of a given array recursively.

class sequence:
    def __init__(self, arry):
        self.arry = arry
        self.len = len(arry)
        self.pointer = 0
   
    def printN(self):
        if self.pointer == self.len-1:
            return self.arry[self.pointer]
        else:
            print(self.arry[self.pointer], end = ', ')
            self.pointer += 1
            return self.printN()

a1 = sequence([1000, 200, 30, 450, -600, 800])
print(a1.printN())