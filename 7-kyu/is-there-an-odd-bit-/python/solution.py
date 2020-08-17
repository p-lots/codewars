def any_odd(x):
    x = f"{x:b}"[::-1]
    for i, ch in enumerate(x):
        if i % 2 == 1 and ch == '1':
            return 1
    return 0