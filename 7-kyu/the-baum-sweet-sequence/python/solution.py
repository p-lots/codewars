def is_baum_sweet(n):
    if n == 0:
        return True
    elif n == 1:
        return True
    n_bin = [group for group in f'{n:b}'.split('1') if len(group) > 0]
    return all(len(group) % 2 == 0 for group in n_bin)

def baum_sweet():
    ret = -1
    while True:
        ret += 1
        yield 1 if is_baum_sweet(ret) else 0
