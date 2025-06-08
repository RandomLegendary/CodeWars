def disemvowel(string_):
    vowels= ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    string_arr = []
    
    
    for letter in string_:
        if letter not in vowels:
            string_arr.append(letter)
​
    print(string_arr)
    
    result = ''.join(string_arr)
    
    return result