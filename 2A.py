
def RotateLeft(source, indx):
    for elem in range(indx):
        var = source[0]
        for x in range(len(source)-1):
            source[x] = source[x+1]
        source[-1] = var
    return source 
source = [10, 20, 30, 40, 50, 60]
RotateLeft(source, 3)

#ans [ 40, 50, 60, 10, 20, 30]

