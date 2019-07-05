import string

def is_valid_IP(strng):
    if not strng or not (strng.count('.') == 3):
        return False
    for n in strng.split('.'):
        if (n[0] == '0' and len(n) > 1) or (not n.isdigit()) or (int(n) > 255 or int(n) < 0):
            return False
    return True