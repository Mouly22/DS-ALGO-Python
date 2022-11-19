def shiftLeft(source, indx):
    for elem in range(indx):
        var = 0
        for x in range(len(source)-1):
            source[x] = source[x+1]
        source[-1] = var
    return source
source = [10, 20, 30, 40, 50, 60]
shiftLeft(source, 3)

#ans: [ 40, 50, 60, 0, 0, 0 ]