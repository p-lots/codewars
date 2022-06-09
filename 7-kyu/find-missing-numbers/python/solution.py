def find_missing_numbers(arr):
    return [n for n in range(min(arr), max(arr) + 1) if n not in arr] if arr else []
