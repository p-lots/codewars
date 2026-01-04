def arbitrate(inp, n):
    if all(digit == '0' for digit in inp):
        return inp
    idx = inp.index('1')
    return f'{"0" * idx}1{"0" * (n - idx - 1)}'
