def convert_bits(a, b):
    return bin(a ^ b)[2:].count('1')