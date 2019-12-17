def minMinMax(arr):
    smallest = min(arr)
    biggest = max(arr)
    ret = smallest + 1
    for i in range(smallest + 1, biggest + 1, 1):
        if i not in arr:
            ret = i
            break
    return [smallest, ret, biggest]