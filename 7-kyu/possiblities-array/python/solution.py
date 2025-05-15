def is_all_possibilities(arr):
    return all(n in range(len(arr)) for n in arr) if arr else False