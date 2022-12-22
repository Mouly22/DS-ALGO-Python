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
  
    
    # if lin = [10, 20, 30, 40, None]
    # then, CircularArray(lin, 2, 4) will generate
    # cir = [40, null, 10, 20, 30]

  # Print from index 0 to len(cir) - 1
  def printFullLinear(self): #Easy
   for idx in range(len(self.cir)):
     if idx == len(self.cir) - 1:
        print(self.cir[idx], end = ' ')
     else:
        print(self.cir[idx], end = ', ')
   
   print()

  # With no null cells
  def linearize(self):
    arr1 = [None]* self.size
    strt = self.start
    for i in range(self.size):
      arr1[i] = self.cir[strt]
      strt = (strt + 1) % len(self.cir)
    self.cir = arr1

lin_arr1 = [10, 20, 30, 40, None]
c1 = CircularArray(lin_arr1, 2, 4)
c1.printFullLinear() # This should print: 40, None, 10, 20, 30
c1.linearize()
c1.printFullLinear() # This should print: 10, 20, 30, 40


