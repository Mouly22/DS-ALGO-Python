#Given base and n that are both 1 or more, compute recursively (no loops) the value of base  to the n power, so powerN(3, 2) is 9 (3 squared). 

def powerN(val, pow):
    if pow == 0:
        return 1
    elif  pow == 1:
        return  val
    else:
        return val * powerN(val, pow - 1)                                                                                                             

print(powerN(3, 5))