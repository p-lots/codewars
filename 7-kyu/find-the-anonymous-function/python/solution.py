def find_function(func, arr):
    found_function = [f for f in func if callable(f)][0]
    return [elem for elem in arr if found_function(elem)]
