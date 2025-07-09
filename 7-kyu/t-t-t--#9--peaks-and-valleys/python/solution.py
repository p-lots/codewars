def peak_and_valley(arr):
    result = []
    for i in range(3, len(arr) - 3):
        curr = arr[i]
        if all(n > curr for n in arr[(i - 3):i]) and all(n > curr for n in arr[(i + 1):(i + 4)]) \
        or all(n < curr for n in arr[(i - 3):i]) and all(n < curr for n in arr[(i + 1):(i + 4)]):
            result.append(curr)
    return result
