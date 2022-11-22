
def remove(source, size, idx):
    y = 0
    if idx >= size:
        return "Input a correct index"
    for x in range(idx, size-1, 1):
        source[x] = source[x+1]

    source[size-1] = 0
    print(source)
 
source = [10, 20, 30, 40, 50, 0, 0]
print(remove(source, 5, 2))

 #Ans  [ 10,20,40,50,0,0,0]
