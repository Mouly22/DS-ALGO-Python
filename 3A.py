
def shiftRight(source, indx):
    for i in range(indx):
        var = 0
        for x in range(len(source)-1, -1, -1):
            source[x] = source[x-1]
        source[0] = var
    print(source)
source = [10, 20, 30, 40, 50, 60]
shiftRight(source, 3)

#ans [ 0,0,0,10,20,30 ]
