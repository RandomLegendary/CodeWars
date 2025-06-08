def odd_or_even(arr):
    length = len(arr)
    temp = 0
    
    result = 0
    
    while length != temp:
        
        result += arr[temp]
        
        temp += 1
        
    if result % 2 == 0:
        return "even"
    else:
        return "odd"