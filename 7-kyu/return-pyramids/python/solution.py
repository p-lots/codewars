def pyramid(n):
    pyramid = []
    for i in range(n):
        before_spaces = ' ' * (n - i - 1)
        between_spaces = ' ' * (i * 2)
        line = f'{before_spaces}/{between_spaces if i < n - 1 else "_" * (i * 2)}\\'
        pyramid.append(line)
    return '\n'.join(pyramid) + '\n'