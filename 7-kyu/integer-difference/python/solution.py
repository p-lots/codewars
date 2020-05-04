def int_diff(arr, n):
    ret = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if i != j and abs(arr[i] - arr[j]) == n:
                ret += 1
    return ret