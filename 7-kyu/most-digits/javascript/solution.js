def find_longest(arr):
    return sorted(arr, key=lambda n: len(str(n)), reverse=True)[0]