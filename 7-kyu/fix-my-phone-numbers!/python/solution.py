import re

def is_it_a_num(s: str) -> str:
    filtered: str = ''.join(ch for ch in s if ch.isdigit())
    if re.match(r'^0\d{10}$', filtered) is None:
        return 'Not a phone number'
    return filtered
    
