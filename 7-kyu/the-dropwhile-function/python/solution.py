def span(arr, pred):
    i = 0
    while i < len(arr):
        if not pred(arr[i]):
            break
        i += 1
    return [arr[:i + 1], arr[i:]]

def drop_while(arr, pred):
    return span(arr, pred)[1]
