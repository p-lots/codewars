def swap_head_tail(arr):
    midpt = len(arr) // 2
    return arr[midpt + (len(arr) % 2):] + [arr[midpt]] * (len(arr) % 2) + arr[:midpt]