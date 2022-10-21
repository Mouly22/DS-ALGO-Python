def split(source):
    #for i in range(4):
    inp = 0
    var = 0
    for i in range(len(source)-1):
        var += source[i]
        inp = var
        source[i] = source[i+1]
        
        #print(var)

    
    
source = [10, 3, 1, 2, 10]
split(source)

def split(source):
    #var1 = 0
    i = 1
    for p in range(len(source)):
        var1 = 0
        var2 = 0

        for elm in range(0,i):
            var1 += source[elm]
        

        
    
        for elm2 in range(i, len(source)):
            var2 += source[elm2] 
       
        
        i += 1
        
        if var1 == var2:
            print('true')
            break
        else:
            print('false')
source = [10, 3, 1, 2, 10]
split(source)