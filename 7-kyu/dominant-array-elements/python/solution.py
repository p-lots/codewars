def solve(arr):
    return [elem for idx, elem in enumerate(arr) if all(elem > n for n in arr[(idx + 1):])]
