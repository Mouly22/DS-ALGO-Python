#given array in assending order[1, 2, 3, 3, 4, 4, 4]
#Output should be 4 as removing will return the array as [1, 2, 3, 4]; need to solve in the existing array
#Solve:
def remove_dup(arr):
    count = 0
    n_arr = [0] * len(arr)
    if len(arr) > 0:
        for elem in range(len(arr)-1):
            if arr[elem] != arr[elem + 1]:
                n_arr[count] = arr[elem]
                count +=1

        n_arr[count] = arr[len(arr)-1]
        count +=1

        return n_arr
    else:
        return 0

arr = [1, 2, 2, 3, 3, 4, 4, 5]
print(remove_dup(arr))


