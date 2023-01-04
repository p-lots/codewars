def is_isogram(string):
    s = set()
    str_lower = string.lower()
    for char in str_lower:
        if char not in s:
            s.add(char)
        else:
            return False
    return True