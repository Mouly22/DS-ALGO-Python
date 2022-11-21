
def RotateRight(source, indx):
    for g in range(indx):
        var = source[-1]
        for x in range(len(source)-1, -1, -1):
            source[x] = source[x-1]
        source[0] = var
    return source
        
    
source = [10, 20, 30, 40, 50, 60]
RotateRight(source, 3)

#Ans  [ 40, 50, 60, 10, 20, 30]
