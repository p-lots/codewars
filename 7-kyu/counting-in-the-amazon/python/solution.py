def count_arara(n):
    return 'anane' if n == 1 else ' '.join('adak' for _ in range(n // 2)) + (' anane' if n % 2 == 1 else '')
    