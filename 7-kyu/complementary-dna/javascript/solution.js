def DNA_strand(dna):
    lookup_table = {'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A'}
    return ''.join(lookup_table[item] for item in dna)