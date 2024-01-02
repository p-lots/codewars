def binary_pyramid(m, n):
    total = sum(int(f'{num:b}') for num in range(m, n + 1))
    return f'{total:b}'
