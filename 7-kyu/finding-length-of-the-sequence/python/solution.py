def length_of_sequence(arr, n):
    if not arr.count(n) == 2:
        return 0
    first_idx = 0
    first_found = False
    second_idx = 0
    for i, val in enumerate(arr):
        if val == n:
            if not first_found:
                first_idx = i
                first_found = True
            elif first_found:
                second_idx = i
                break
    return second_idx - first_idx + 1