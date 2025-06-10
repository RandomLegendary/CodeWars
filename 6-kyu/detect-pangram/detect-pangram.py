def is_pangram(st):
    alph = list('abcdefghijklmnopqrstuvwxyz')
    str = st.lower()
    
    for each in alph:
        if each not in str:
            return False
    return True