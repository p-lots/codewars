def get_char_sum(strng):
    return 0 if strng is None or any(not ch.isalpha() for ch in strng) else \
        sum(ord(ch.upper()) for ch in strng)

def compare(s1, s2):
    return get_char_sum(s1) == get_char_sum(s2)