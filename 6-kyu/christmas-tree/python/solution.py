def christmas_tree(height):
    return '\n'.join([f'{" " * (height - i - 1)}{"*" * (i * 2 + 1)}{" " * (height - i - 1)}' for i in range(height)])
