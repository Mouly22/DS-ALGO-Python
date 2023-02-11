def bin_src(lst, val, low, high):
    mid = (low+high)//2
    if lst[mid] == val:
        return mid
    elif low == high:
        return None
    else:
        if lst[mid] > val:
            return bin_src(lst, val, low, mid)
            
        else:
            return bin_src(lst, val, mid+1, high)
            
lst = [10, 20, 40, 50, 70, 150, 170]   
print(bin_src(lst, 70, 0, len(lst)-1))






#Binary Search iterative
def bin_src(lst, val):
    low = 0
    high = len(lst) -1
    
    while True:
        mid = (low+high)//2
        if low == high:
            break
            return -1
        elif lst[mid] == val:
            return mid
        elif lst[mid] > val:
            high = mid
        else:
            low = mid + 1
    
    
    
lst = [10, 20, 40, 50, 70, 150, 170, 230]   
print(bin_src(lst, 70))