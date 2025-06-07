def tribonacci(signature, n):
    if n == 0:
        return []
    else:
        
        result = [signature[0], signature[1], signature[2]]
        
        temp = 0
        
        while n != temp + 3:     
            if n == temp + 4:
                result_temp = result[0+temp] + result[1+temp]
                result.append(result_temp)
                temp += 1
            else:
                result_temp = result[0+temp] + result[1+temp] + result[2+temp] 
                result.append(result_temp)
                temp += 1
        
        return result