# Consider an array named source. Write a method/function named removeAll( source, size, element) that removes all the occurrences of the given element in the source array. You must execute the method by passing an array, its size and the element to be removed. After calling the method, print the array to show whether all the occurrences of the element have been removed properly.
# Example:
# source=[10,2,30,2,50,2,2,0,0]
# removeAll(source,7,2)
# After calling removeAll(source,7,2), all the occurrences of 2 must be removed. Printing the array afterwards should give the output as: 
#  [ 10,30,50,0,0,0,0,0,0]
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
