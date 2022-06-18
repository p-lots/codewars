def smaller(arr):
    return [sum(num < n for num in arr[i + 1:]) for i, n in enumerate(arr)]
