def ascii_encrypt(plaintext):
    return ''.join([chr(ord(ch) + i) for i, ch in enumerate(plaintext)])

def ascii_decrypt(plaintext):
    return ''.join([chr(ord(ch) - i) for i, ch in enumerate(plaintext)])