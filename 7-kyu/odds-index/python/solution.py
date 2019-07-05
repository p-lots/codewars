def odd_ball(arr):
    for item in arr:
        if type(item) == int and item < len(arr) and arr[item] == 'odd':
            return True
    return False