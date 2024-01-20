def correct_polish_letters(st): 
    lookup_table = { 'ą': 'a', 'ć': 'c', 'ę': 'e', 
        'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 
        'ź': 'z', 'ż': 'z'
    }
    return ''.join(lookup_table.get(ch, ch) for ch in st)