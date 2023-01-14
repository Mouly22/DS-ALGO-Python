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


  # the method take another circular array and returns a linear array containing the common elements between the two circular arrays.

  def intersection(self, c2):
    count = 0
    count2 = 0
    val = 0
    st1 = self.start
    st2 = c2.start
    arr = [None]* (len(self.cir))
    for p in range(len(self.cir)):
      for q in range(len(c2.cir)):
        if self.cir[st1] != None and self.cir[st1] == c2.cir[st2]:
          flag = True
          for res in range(len(arr)):
            if arr[res] == c2.cir[st2]:
              flag = False
              break
          if flag == True:
            arr[count] = c2.cir[st2]
            count += 1
            val = count
            break
        st2 = (st2 + 1) % len(c2.cir)
      st2 = c2.start
      st1 = (st1 + 1)% len(self.cir)
        
    arr2 = [None]* val
    for i in arr:
      if i != None:
        arr2[count2] = i
        count2 += 1

    return arr2


lin_arr9 = [10, 20, 30, 40, 50, None, None, None]
c10 = CircularArray(lin_arr9, 5, 5)
c10.printFullLinear() # This should print: 40, 50, None, None, None, 10, 20, 30
lin_arr10 = [5, 40, 15, 25, 10, 20, 5, None, None, None, None, None]
c11 = CircularArray(lin_arr10, 8, 7)
c11.printFullLinear() # This should print: 10, 20, 5, None, None, None, None, None, 5, 40, 15, 25
output = c10.intersection(c11)
print(output) # This should print: [10, 20, 40]