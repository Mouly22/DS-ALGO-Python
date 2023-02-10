
def lefttriangle(number, inc):
    sum = number+ inc
    if number <= 0:
        return 1
    else:
        increment(inc, number, sum)
        lefttriangle(number - 1, inc +1)

def increment(count,number,sum):
    if count <= 0:
        return 1
    else:
        increment(count - 1,number, sum)
        if count+number == sum:
            print(count)
        else:
            print(count, end = ' ')


lefttriangle(5, 1)


#output
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5