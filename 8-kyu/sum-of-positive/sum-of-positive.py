def positive_sum(arr):
    
    result = []
    
    for element in arr:
        if element > 0:
            result.append(element)
            
    return sum(result)