def decode(strng):
    if strng.isdigit():
        return chr(int(strng))
    first_char = ''
    first_char_in_strng_pos = 0
    first_time = True
    for i, ch in enumerate(strng):
        if ch.isdigit():
            first_char += ch
        elif ch.isalpha() and first_time:
            first_char_in_strng_pos = i
            first_time = False
            break
    first_char = chr(int(first_char))
    ret = first_char + strng[first_char_in_strng_pos:]
    if len(ret) == 2:
        return ret
    elif len(ret) == 3:
        return f'{ret[0]}{ret[-1]}{ret[1]}'
    return f'{ret[0]}{ret[-1]}{ret[2:-1]}{ret[1]}'

def decipher_this(strng):
    return ' '.join(decode(word) for word in strng.split())