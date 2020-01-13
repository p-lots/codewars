from math import fmod

def check_func(item):
    return type(item) == int or (type(item) == float and fmod(item, 1.0) == 0.0)

def is_int_array(arr):
    if type(arr) == list:
        if len(arr) == 0:
            return True
        return all(check_func(item) for item in arr)
    return False