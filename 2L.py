# Consider an array named source. Write a method/function named rotateLeft( source, k) that rotates all the elements of the source array to the left by 'k' positions. You must execute the method by passing an array and number of cells to be shifted. After calling the method, print the array to show whether the elements have been shifted properly.
# Example: source=[10,20,30,40,50,60]
# rotateLeft(source,3)
# After calling rotateLeft(source,3), printing the array should give the output as:  [ 40, 50, 60, 10, 20, 30]
def RotateLeft(source, indx):
    for elem in range(indx):
        var = source[0]
        for x in range(len(source)-1):
            source[x] = source[x+1]
        source[-1] = var
    return source 
source = [10, 20, 30, 40, 50, 60]
RotateLeft(source, 3)
