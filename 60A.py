#Maximum Sum COntigunous Subarray
def max_con_sub(arr):
    temp = 0
    max_sum = 0
    for i in range(len(arr)):
        temp += arr[i]
        if temp > max_sum:
            max_sum = temp 
        else:
            pass
        if temp < 0:
            temp = 0
        else:
            temp = temp

    print(max_sum)       


arr = [-1, -2, 1, 2, 3, -5, 4, 5]
max_con_sub(arr)