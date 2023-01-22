def decode_pass(pass_list, bits):
    password = ''.join(chr(int(bit, 2)) for bit in bits.split())
    return password if password in pass_list else False
