def binary_to_string(binary):
    return ''.join(chr(int(n, 2)) for n in binary[2:].split('0b'))