def pattern(n):
    return '\n'.join(f'1{"*" * i}{i + 1 if i > 0 else ""}' for i in range(n))
