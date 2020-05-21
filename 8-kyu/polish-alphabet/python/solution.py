def correct_polish_letters(strng): 
    lookup_table = { 'ą': 'a', 'ć': 'c', 'ę': 'e', 
        'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 
        'ź': 'z', 'ż': 'z'
    }
    return ''.join(lookup_table[ch] if ch in lookup_table else ch for ch in strng)