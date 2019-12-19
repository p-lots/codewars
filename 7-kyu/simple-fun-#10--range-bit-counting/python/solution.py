def range_bit_count(a, b):
    return sum(f'{n:b}'.count('1') for n in range(a, b + 1))