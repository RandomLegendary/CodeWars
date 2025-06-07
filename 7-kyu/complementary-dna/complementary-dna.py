def DNA_strand(dna):
    length = len(dna)
    temp = 0 
    
    result = []
    
    while length != temp:
        if dna[temp] == 'A':
            result.append('T')
        elif dna[temp] == 'T':
            result.append('A')
        elif dna[temp] == 'C':
            result.append('G')
        else:
            result.append('C')
        temp += 1
        
    return "".join(result)