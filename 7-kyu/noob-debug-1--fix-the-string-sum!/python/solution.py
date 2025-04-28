def encode(strng):
    return sum(ord(ch) for ch in strng)

def add(s1, s2):
    return encode(s1) + encode(s2)