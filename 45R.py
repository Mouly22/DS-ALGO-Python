#Implement a recursive algorithm to find the n-th Fibonacci number.

def fibN(val):
    if val <= 0:
        return 0
    if val == 1:
        return 1
    if val > 1:
        return fibN(val - 1) + fibN(val - 2)

print(fibN(7))