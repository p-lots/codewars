import string

def is_valid_password(s):
    return any(ch in string.ascii_lowercase for ch in s) and any(ch in string.ascii_uppercase for ch in s) \
        and any(ch in '0123456789' for ch in s) and any(ch in '!@#$%^&*?' for ch in s) \
        and all(ch in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?' for ch in s)

def check_password(s):
    print(s)
    if not (8 <= len(s) <= 20):
        return 'not valid'
    return 'valid' if is_valid_password(s) else 'not valid'