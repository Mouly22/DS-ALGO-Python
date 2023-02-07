# A "bunch" in an array is a consecutive chain of two or more adjacent elements of the same value. Write a method that returns the number of elements in the largest bunch found in the given array.
# Input: [1, 2, 2, 3, 4, 4, 4]   Output: 3
# Explanation: There are two bunches here {2,2} and {4,4,4}. The largest bunch is {4,4,4} containing 3 elements so 3 is returned.
# Input: [1,1,2, 2, 1, 1,1,1] Output:4
#  Explanation: There are three bunches here {1,1} and {2,2} and {1,1,1,1}. The largest bunch is {1,1,1,1} containing 4 elements so 4 is returned.
def MaxBunch(source):
    count = 1
    temp = None
    store = None
    narray = []
    for i in range(len(source)):
        if temp == None and store == None:
            temp = source[i]
            store = 1
        elif source[i] == temp:
            count += 1

            if store < count:              
                store = count
        else:
            count = 1
            temp = source[i]
    return store

source =  [1, 2, 2, 3, 4, 4, 4]
print(MaxBunch(source))
