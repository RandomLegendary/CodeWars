def digital_root(n):
    
    strn = str(n)
    
    length = len(strn)
    temp = 0
    
    result = 0
    
    while temp != length:
        result += int(strn[temp])
        temp += 1
        
    while result >= 10:
        temp = 0
        
        new_result = 0
        
        strn = str(result)
        length = len(strn)
        while temp != length:
            new_result += int(strn[temp])
            temp += 1
        
        result = new_result
        
    return result