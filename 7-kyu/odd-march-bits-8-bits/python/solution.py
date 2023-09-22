def bit_march (n: int) -> list:
    ones = 2 ** n - 1
    ret = []
    while ones < 2 ** 8:
        ones_str = f'{ones:08b}'
        ones_lst = [int(digit) for digit in ones_str]
        ret.append(ones_lst)
        ones <<= 1
    return ret
