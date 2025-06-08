def find_average(numbers):
    if numbers == []:
        return 0
    else:
        
        length = len(numbers)
        
        result = 0
        
        for each in numbers:
            result += each
            
        end = result / length
        
        return end