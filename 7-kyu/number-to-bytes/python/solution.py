def to_bytes(n):
    n_bin = f'{n:b}'
    while len(n_bin) % 8 != 0:
        n_bin = '0' + n_bin
    return [n_bin[i:i + 8] for i in range(0, len(n_bin), 8)]
