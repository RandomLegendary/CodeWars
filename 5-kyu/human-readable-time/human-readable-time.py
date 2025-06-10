def make_readable(seconds):
    
    hours = str(seconds // 3600)
    if len(hours) == 1:
        hours = '0' + hours
    minutes = str((seconds % 3600) // 60)
    if len(minutes) == 1:
        minutes = '0' + minutes
    seconds = str(((seconds % 3600) % 60))
    if len(seconds) == 1:
        seconds = '0' + seconds
    
    return hours +':'+ minutes +':'+ seconds