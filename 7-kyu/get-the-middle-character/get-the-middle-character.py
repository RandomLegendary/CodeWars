def get_middle(s):
    if (len(s) + 1) % 2 == 1:
        return s[int((len(s) -1) / 2)] + s[int((len(s)) / 2)]
    else:
        return s[int((len(s)) / 2)] 