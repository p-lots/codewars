def sort_by_value_and_index(arr):
    sort_key = [(n, n * i) for i, n in enumerate(arr, 1)]
    return [n for n, _ in sorted(sort_key, key=lambda pair: pair[1])]
