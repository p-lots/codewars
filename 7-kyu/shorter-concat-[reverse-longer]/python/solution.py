def shorter_reverse_longer(a, b):
    short, long = min(a, b, key=len), max(a, b, key=len)
    if len(a) == len(b):
        short = b
        long = a
    return f'{short}{long[::-1]}{short}'
