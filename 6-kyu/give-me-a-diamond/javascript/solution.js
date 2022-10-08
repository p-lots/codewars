def diamond(n):
    if n % 2 == 0 or n < 1:
        return None
    ret = ''
    spaces_before = n // 2
    for num_stars in range(1, n + 1, 2):
        ret += ' ' * spaces_before + '*' * num_stars + '\n'
        spaces_before -= 1
    spaces_before = 1
    for num_stars in range(n - 2, 0, -2):
        ret += ' ' * spaces_before + '*' * num_stars + '\n'
        spaces_before += 1
    return ret
        