def are_you_playing_banjo(name):
    
    yes = " plays banjo" 
    no = " does not play banjo"
    lowername = name.lower()
    if lowername.startswith('r'):
        return name + yes
    else:
        return name + no