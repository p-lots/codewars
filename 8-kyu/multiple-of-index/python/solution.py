def multiple_of_index(arr):
    return [n for i, n in enumerate(arr) if i > 0 and n % i == 0]