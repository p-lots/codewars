def handler(key, is_caps=False, is_shift=False):
    valid_keys = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    if not (type(key) == str) or not 0 < len(key) < 2 or key not in valid_keys:
        return 'KeyError'
    if key.isalpha():
        if is_caps and is_shift:
            return key
        if is_caps ^ is_shift:
            return key.upper()
        return key
    nonalpha_lookup = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^',
                       '7': '&', '8': '*', '9': '(', '0': ')', '`': '~', '-': '_',
                       '=': '+', '[': '{', ']': '}', '\\': '|', ';': ':', "'": '"', 
                       ',': '<', '.': '>', '/': '?'}
    return nonalpha_lookup[key] if is_shift else key
