def find_outlier(integers):
    first_result = integers[0] % 2
    second_result = integers[1] % 2 
    if first_result == second_result:
        if first_result == 0:  
            for each in integers:
                if each % 2 == 1:
                    return each
        else:
            for each in integers:
                if each % 2 == 0:
                    return each
    else:
        third_result = integers[2] % 2
        if first_result == third_result:
            return integers[1]
        else:
            return integers[0]