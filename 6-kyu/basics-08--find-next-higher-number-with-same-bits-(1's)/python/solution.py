def next_higher(value):
    nxt = value + 1
    while f'{nxt:b}'.count('1') != f'{value:b}'.count('1'):
        nxt += 1
    return nxt