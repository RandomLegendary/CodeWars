def descending_order(num):
    li = list(str(num))
    maxnum = int(max(li))
    
    li2 = []
    
    for each in li:
        li2.append(int(each))
    
    
    endli = []
    
    tempcount = 0
    
    while maxnum != -1:
        if maxnum in li2:
            
            if li2.count(maxnum) > 0:
                while tempcount != li2.count(maxnum):
                    endli.append(maxnum)
                    li2.remove(maxnum)
                    continue 
                    
            else:
                endli.append(maxnum)
                li2.remove(maxnum)
        
        maxnum -= 1
            
    endli2 = []
    for each in endli:
        endli2.append(str(each))
    
    return int("".join(endli2))