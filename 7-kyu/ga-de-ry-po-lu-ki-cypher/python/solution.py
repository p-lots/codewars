LOOKUP_TABLE = {'g': 'a', 'a': 'g', 'd': 'e', 'e': 'd', 'r': 'y',
                'y': 'r', 'p': 'o', 'o': 'p', 'l': 'u', 'u': 'l',
                'k': 'i', 'i': 'k'
               }

def encode(message):
    ret = ''
    for ch in message:
        if ch.lower() in LOOKUP_TABLE.keys():
            if ch.islower():
                ret += LOOKUP_TABLE[ch]
            else:
                ret += LOOKUP_TABLE[ch.lower()].upper()
        else:
            ret += ch
    return ret

def decode(message):
    return encode(message)
