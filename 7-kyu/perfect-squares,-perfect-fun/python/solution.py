def is_perfect_sq(n):
    n_str = str(n)
    return int(len(n_str) ** 0.5) ** 2 == len(n_str)

def square_it(digits):
    if not is_perfect_sq(digits):
        return 'Not a perfect square!'
    digits_str = [n for n in str(digits)]
    ret = []
    root = int(len(digits_str) ** 0.5)
    for i in range(root):
        row = []
        for j in range(root):
            row.append(digits_str[i * root + j])
        ret.append(row)
    return '\n'.join(''.join(n for n in row) for row in ret)
