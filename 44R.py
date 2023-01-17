#Implement a recursive algorithm to find factorial of n.

def factor(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factor(n-1)
    
    
print(factor(6))