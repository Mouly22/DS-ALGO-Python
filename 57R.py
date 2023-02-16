def harmonic_sum(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    else:
        return (1/val) + harmonic_sum(val-1)
        
    
print(harmonic_sum(4))