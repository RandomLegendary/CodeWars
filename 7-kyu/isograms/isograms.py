def is_isogram(string):
    stringlow = string.lower()
    lst = list(stringlow)
    
    list_alpha = list('abcdefghijklmnopqrstuvwxyz')
    
    for element in lst:
        if element in list_alpha:
            list_alpha.remove(element)
        else:
            return False
        
    return True