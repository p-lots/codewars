def even_chars(st):
    return 'invalid string' if len(st) > 100 or len(st) < 2 else [ch for i, ch in enumerate(st, 1) if i % 2 == 0]