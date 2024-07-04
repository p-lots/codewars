def transpose_two_strings(arr):
    left, right = arr
    while len(left) < len(right):
        left += ' '
    while len(right) < len(left):
        right += ' '
    return '\n'.join(f'{lhs} {rhs}' for lhs, rhs in zip(left, right))
