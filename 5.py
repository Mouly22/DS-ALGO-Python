#  Consider an array named source. Write a method/function named remove( source, size, idx) that removes the element in index idx of the source array. You must execute the method by passing an array, its size and the idx( that is the index of the element to be removed). After calling the method, print the array to show whether the element of that particular index has been removed properly.
# Example:
# source=[10,20,30,40,50,0,0]
# remove(source,5,2)
# After calling remove(source,5,2) , printing the array should give the output as: 
#  [ 10,20,40,50,0,0,0]
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
