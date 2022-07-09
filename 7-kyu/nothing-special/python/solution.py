def nothing_special(s):
    return 'Not a string!' if not isinstance(s, str) else ''.join(ch for ch in s if ch.isalpha() or ch.isdigit() or ch.isspace())
