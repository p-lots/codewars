from math import ceil

def new_avg(arr, newavg):
    result = ceil(newavg * (len(arr) + 1) - sum(arr))
    if result > 0:
        return result
    else:
        raise ValueError