def stray(arr):
    length = len(arr)
    temp = 0
    
    while temp != length:
           
        if arr.count(arr[temp]) == 1:
            return arr[temp]
        
        temp +=1