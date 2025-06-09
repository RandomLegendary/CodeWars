import math
​
def is_square(n): 
    if n < 0:
        return False
    else:
        root = math.sqrt(n)
        if str(root).endswith(".0"):
            return True
        else: 
            return False