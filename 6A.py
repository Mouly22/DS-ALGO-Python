
def removeAll(source, size, element):
    count = 0
    narray = [0]* len(source)
    for x in range(len(source)):
        if source[x] == element:
            continue
        else:
            narray[count] = source[x]
        count += 1
        
        if count >= size:
            break
            
    source = narray
    return source
            
    
source=[10,2,30,2,50,2,2,0,0]
removeAll(source,7,2)
#ans  [ 10,30,50,0,0,0,0,0,0]
