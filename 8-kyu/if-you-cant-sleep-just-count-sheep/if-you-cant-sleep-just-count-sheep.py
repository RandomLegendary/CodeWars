 
def count_sheep(n):
    temp = 1
    result = ''
    while temp != n + 1:
        result += f'{temp} sheep...'
        temp += 1
    return result