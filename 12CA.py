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

lin_arr1 = [10, 20, 30, 40, None]
c1 = CircularArray(lin_arr1, 2, 4)
c1.printForward() # This should print: 10, 20, 30, 40