#Implement a recursive algorithm that takes a decimal number n and converts n to its corresponding (you may return as a string) binary number.

def binarymaker(val):
    if val == 1:
        print(f'{1}', end ='')
    elif val ==0:
        print(f'{0}', end ='')
    else:
        if val % 2 == 0:
            binarymaker(val//2)
            print(f'{0}', end = '')
        else:
            binarymaker(val//2)
            print(f'{1}', end ='')

binarymaker(100)