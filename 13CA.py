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

  def printBackward(self):
    k = (self.start + self.size - 1) % len(self.cir)
    for i in range(self.size):
      if i == self.size-1:
        print(self.cir[k], end = ' ')
      else:
        print(self.cir[k], end = ', ')
      k = k - 1
      if k < 0:
        k = len(self.cir) - 1
    print()

lin_arr1 = [10, 20, 30, 40, None]
c1 = CircularArray(lin_arr1, 2, 4)
c1.printBackward() # This should print: 40, 30, 20, 10

    