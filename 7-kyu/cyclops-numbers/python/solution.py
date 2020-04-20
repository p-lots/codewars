def cyclops(n):
    n = f'{n:b}'.split('0')
    return len(n) == 2 and len(n[0]) == len(n[1])