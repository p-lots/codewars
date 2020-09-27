def encode(strng):
    return ''.join(bin(ord(ch))[2:].zfill(8).replace('0', '000').replace('1', '111') for ch in strng)

def decode(bits):
    ascii = ['0' if bits[i:i + 3].count('0') >= 2 else '1' for i in range(0, len(bits), 3)]
    ret = [''.join(ascii[i:i + 8]) for i in range(0, len(ascii), 8)]
    return ''.join(chr(int(elem, 2)) for elem in ret)