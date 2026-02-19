def find_all(array, n):
    positions = [i if x == n else -1 for i, x in enumerate(array)]
    return list(filter(lambda item: item != -1, positions))