def swap_vowel_case(st): 
    ret = ''
    for ch in st:
        if ch.lower() in 'aeiou':
            if ch.islower():
                ret += ch.upper()
            else:
                ret += ch.lower()
        else:
            ret += ch
    return ret
