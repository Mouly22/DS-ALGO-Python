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

    # Print from index 0 to len(cir) - 1
  def printFullLinear(self): #Easy
   for idx in range(len(self.cir)):
     if idx == len(self.cir) - 1:
        print(self.cir[idx], end = ' ')
     else:
        print(self.cir[idx], end = ', ')
   
   print()
 
  # Do not change the Start index
  def resizeStartUnchanged(self, newcapacity): #Medium
    new_cir = [None]* newcapacity
    k = self.start
    indx = self.start
    for p in range(self.size):
      new_cir[indx] = self.cir[k]
      k = (k+1) % len(self.cir)
      indx = (indx+ 1) % len(new_cir)
    self.cir = new_cir

lin_arr2 = [10, 20, 30, 40, 50]
c2 = CircularArray(lin_arr2, 2, 5)
c2.printFullLinear() # This should print: 40, 50, 10, 20, 30
c2.resizeStartUnchanged(8) # parameter --> new Capacity
c2.printFullLinear() # This should print: None, None, 10, 20, 30, 40, 50, None