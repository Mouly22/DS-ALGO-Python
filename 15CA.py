class CircularArray:
  def __init__(self, lin, st, sz):
    # Initializing Variables
    self.start = st
    self.size = sz
    self.cir = [None]* len(lin)
    val = st
    for idx in range(sz):
      self.cir[val] = lin[idx]
      val = (val+1)%len(lin)


# This method will check whether the array is palindrome or not

  def palindromeCheck(self): #Hard
    var1 = self.start
    var2 = (self.start + self.size - 1) % len(self.cir)
    for i in range(self.size):
      if self.cir[var1] == self.cir[var2]:
        pass
      else:
        print("This array is NOT a palindrom")
        return 
      var1 = (var1 + 1) % len(self.cir)
      var2 = var2 - 1
      if var2 < 0:
        var2 = len(self.cir) - 1
    print("This array is a Palindrome")

lin_arr3 = [10, 20, 30, 20, 10, None, None]
c3 = CircularArray(lin_arr3, 3, 5)
c3.palindromeCheck() # This should print: This array is a palindrome

lin_arr4 = [10, 20, 30, 20, None, None, None]
c4 = CircularArray(lin_arr4, 3, 4)
c4.palindromeCheck() # This should print: This array is NOT a palindrome  

