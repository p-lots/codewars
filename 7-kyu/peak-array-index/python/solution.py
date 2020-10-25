def peak(arr):
    for i in range(len(arr)):
        l_sum = sum(arr[:i])
        r_sum = sum(arr[i + 1:])
        if l_sum == r_sum:
            return i
    return -1