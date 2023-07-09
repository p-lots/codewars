def evil(n):
    return "It's Evil!" if f'{n:b}'.count('1') % 2 == 0 else "It's Odious!"