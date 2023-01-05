

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



  def printForward(self):
    g = self.start
    for idx in range(self.size):
      if idx == self.size-1:
        print(self.cir[g], end = ' ')
      else:
        print(self.cir[g], end = ', ')
      g = (g+1) % len(self.cir)
    print()

  def sort(self):
    
    for p in range(self.size):
      k = self.start
      for q in range(0, (self.size) - p -1):
        var = (k +1) % len(self.cir)
        if self.cir[k] > self.cir[var]:
          value = self.cir[k]
          self.cir[k] = self.cir[var]
          self.cir[var] = value
        k = (k+1) % len(self.cir)



lin_arr5 = [10, 20, -30, 20, 50, 30, None]
c5 = CircularArray(lin_arr5, 5, 6)
c5.printForward() # This should print: 10, 20, -30, 20, 50, 30
c5.sort()
c5.printForward() # This should print: -30, 10, 20, 20, 30, 50

