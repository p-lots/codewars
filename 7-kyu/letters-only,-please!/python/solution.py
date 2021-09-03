def remove_chars(s):
    return ''.join(ch for ch in s if ch.isspace() or ch.isalpha())
