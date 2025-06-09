def move_zeros(lst):
    count = lst.count(0)
    temp = 0
    
    while temp != count:
        lst.remove(0)
        temp += 1
    
    temp2 = count
    
    while temp2 != 0:
        lst.append(0)
        temp2 -= 1
        
    return lst