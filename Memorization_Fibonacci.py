class memorization:
    def __init__(self, value):
        self.fn = [None]*(value + 1)
        
    def fibonacci(self, value):
        if value <= 1:
            self.fn[value] = value
            return value
        elif value in self.fn:
            return self.fn[value]
        else:
            temp = self.fibonacci(value - 1)+ self.fibonacci(value - 2)
            self.fn[value] = temp
            return temp
            
            
a1 = memorization(10)
print(a1.fibonacci(7))
            
