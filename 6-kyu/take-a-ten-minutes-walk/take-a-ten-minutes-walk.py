def is_valid_walk(walk):
    n_counter = 0
    e_counter = 0
    
    length_list = len(walk)
    temp = 0
​
    while length_list != temp:
        if walk[temp] == 'n':
            n_counter += 1
        elif walk[temp] == 'e':
            e_counter += 1
        elif walk[temp] == 's':
            n_counter -= 1
        else:
            e_counter -= 1
        temp += 1
        
    if n_counter == 0 and e_counter == 0 and length_list == 10:
        return True
    else:
        return False