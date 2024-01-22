def array_packing(arr):
    while len(arr) < 4:
        arr.append(0)
    return sum(digit * 2 ** (8 * (len(arr) - idx - 1)) for idx, digit in enumerate(arr[::-1]))