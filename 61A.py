def max_difference(arr):
    store = 0
    for i in range(1, len(arr)):
        d = arr[i] - arr[i-1]
        if d > store:
            store = d
        else:
            store = store
    print(store)
    
        

arr = [3, 5, 4, 2]
max_difference(arr)