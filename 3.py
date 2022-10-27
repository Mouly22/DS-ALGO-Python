# Shift Right k Cells   
# Consider an array named source. Write a method/function named shifRight( source, k) that shifts all the elements of the source array to the right by 'k' positions. You must execute the method by passing an array and number of cells to be shifted. After calling the method, print the array to show whether the elements have been shifted properly.
# Example: source=[10,20,30,40,50,60]
# shiftRight(source,3)
# After calling shiftRight(source,3), printing the array should give the output as: [ 0,0,0,10,20,30 ]
def shiftRight(source, indx):
    for i in range(indx):
        var = 0
        for x in range(len(source)-1, -1, -1):
            source[x] = source[x-1]
        source[0] = var
    print(source)
source = [10, 20, 30, 40, 50, 60]
shiftRight(source, 3)
