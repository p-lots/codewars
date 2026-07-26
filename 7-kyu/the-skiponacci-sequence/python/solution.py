def skiponacci(n):
    a = 0
    b = 1
    skips = ['1']
    i = 1
    while i < n:
        nxt = f'{a + b}' if i % 2 == 0 else 'skip'
        a, b = b, a + b
        skips.append(nxt)
        i += 1
    return ' '.join(skips)