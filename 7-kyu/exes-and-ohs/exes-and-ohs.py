def xo(s):
    
    s_new = s.lower()
    
    amount_x = s_new.count("x")
    amount_o = s_new.count("o")
    
    if amount_x == amount_o:
        return True
    else: 
        return False