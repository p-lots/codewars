def reverse_bits(n):
    b = bin(n)[2:]
    b = b[::-1]
    return int(b, 2)