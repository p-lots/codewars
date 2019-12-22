def check_exam(arr1, arr2):
    return max(0, sum(4 if pair[0] == pair[1] else 0 if len(pair[1]) == 0 else -1 for pair in zip(arr1, arr2)))