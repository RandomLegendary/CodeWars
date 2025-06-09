def find_missing_letter(chars):
    alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    cap = False
    
    if chars[0].isupper() == True:
        cap = True
    
    counter = 0
    
    first_element = chars[counter].lower()
    
    first_element_place_in_alph = alph.index(first_element)    
    
    while True:
        if chars[counter].lower() == alph[counter + first_element_place_in_alph]:
            counter += 1
​
        else:
            if cap == True:
                return alph[counter + first_element_place_in_alph].capitalize()
            else:
                return alph[counter + first_element_place_in_alph]
        
            break