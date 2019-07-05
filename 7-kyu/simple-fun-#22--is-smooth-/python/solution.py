def is_smooth(arr):
    if len(arr) > 2:
        if len(arr) % 2 == 1:
            middle = arr[len(arr) // 2]
        else:
            middle = arr[len(arr) // 2] + arr[len(arr) // 2 - 1]
    else:
        middle = arr[0] + arr[1]
    return middle == arr[0] and middle == arr[-1] and arr[0] == arr[-1]