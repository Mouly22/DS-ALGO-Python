#equivalent
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


    # Print from start index and total size elements
  def printForward(self):
    g = self.start
    for idx in range(self.size):
      if idx == self.size-1:
        print(self.cir[g], end = ' ')
      else:
        print(self.cir[g], end = ', ')
      g = (g+1) % len(self.cir)
    print()
 
 
  def equivalent(self, cir_arr):
    k = self.start
    m = cir_arr.start
    for elm in range(self.size):
      if self.cir[k] != cir_arr.cir[m]:
        return False  
      k = (k+1)% len(self.cir)
      m = (m+1) % len(cir_arr.cir)
    return True


lin_arr6 = [10, 20, -30, 20, 50, 30, None]
c6 = CircularArray(lin_arr6, 2, 6)
c7 = CircularArray(lin_arr6, 5, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c7.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c7)) # This should print: True


lin_arr8 = [10, 20, 30, 40, 50, 60, None, None, None]
c9 = CircularArray(lin_arr8, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c9.printForward() # This should print: 10, 20, 30, 40, 50, 60
print(c6.equivalent(c9)) # This should print: False