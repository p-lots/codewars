from math import floor

def sum_average(arr):
    return floor(sum(sum(subarr) / len(subarr) for subarr in arr))