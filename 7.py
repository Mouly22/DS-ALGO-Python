# Suppose the elements of an array A containing positive integers, denote the weights in kilograms. And we have a beam balance. We want to put the weights on both pans of the balance in such a way that for some index 0 < i < A.length - 1, all values starting from A[0], A[1], upto A[ i - 1], should be on the left pan. And all values starting from A[ i ] upto A[ A.length - 1] should be on the right pan and the left and right pan should be balanced. If such an i exists, return true . Else, return false. 
# Input: [1, 1, 1, 2, 1]	Output : true
# Explanation: (summation of [1, 1, 1] = summation of [2,1])
# Input: [2, 1, 1, 2, 1] Output: false
# Input: [10, 3, 1, 2, 10]  Output: true 
# Explanation: (summation of [10, 3] = summation of [1,2,10]))
def split(source):
    i = 1
    for p in range(len(source)):
        var1 = 0
        
        for elm in range(0,i):
            var1 += source[elm]  
            
        var2 = 0
        for elm2 in range(i, len(source)):
            var2 += source[elm2]   
        i += 1     
        if var1 == var2:
            res ='true'
            break
        else:
            res = 'false'        
    print(res)          
source =  [10, 3, 1, 2, 10] 
split(source)
