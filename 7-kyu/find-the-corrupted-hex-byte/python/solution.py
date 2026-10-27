HEX = set("0123456789ABCDEF")

def find_corrupted_byte(dump):
    for idx, byte in enumerate(dump):
        if any(bit not in HEX for bit in byte) or len(byte) != 2:
            return idx
    return -1