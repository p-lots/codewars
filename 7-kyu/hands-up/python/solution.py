def convert_to_base_three(n):
    if n == 0:
        return [0]
    ret = []
    while n != 0:
        ret.append(n % 3)
        n //= 3
    return ret

def get_positions(n):
    ret = convert_to_base_three(n)[:3]
    if n <= 3:
        ret.append(0)
    return tuple(ret)
