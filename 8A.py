# Write a method that takes an integer value n as a parameter. Inside the method, you should create an array of length n squared (n*n) and fill the array with the following pattern. Return the array at the end and print it.
# If,
# n=2: { 0,1,   2,1 } (spaces have been added to show two distinct groups).
# n=3 : { 0, 0, 1,    0, 2, 1,    3, 2, 1 } ((spaces have been added to show three distinct 
# groups).
# n=4 : {0, 0, 0, 1,   0, 0, 2, 1,    0, 3, 2, 1,   4, 3, 2, 1}  (spaces have been added to show four distinct groups).

def ArraySeries(n):
    narray = (n*n)*[0]
    temp = 1
    for i in range(n-1, len(narray), n):
        for inc in range(temp):
            narray[i- inc] = inc + 1
        temp += 1
    return narray 

print(ArraySeries(4))