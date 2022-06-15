def hamming_distance(a, b):
    return bin(int(a, 2) ^ int(b, 2)).count('1')