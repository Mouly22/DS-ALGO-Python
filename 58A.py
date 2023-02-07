#given array in assending order[1, 2, 3, 3, 4, 4, 4]
#Output should be 4 as removing will return the array as [1, 2, 3, 4]; need to solve in the existing array
#Solve:

def remove_duplicate_count1(arr):
    if len(arr) > 0:
        count = 0
        for i in range(len(arr)-1):
            if arr[i] != arr[i + 1]:
                arr[count] = arr[i]
                count +=1

        arr[count] = arr[len(arr)-1]
        count +=1
        return count
    else:
        return 0
        

arr = [2, 2, 4, 5, 5, 7, 8, 8, 8]     #Output: 5
print(remove_duplicate_count1(arr))