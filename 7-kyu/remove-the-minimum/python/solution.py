import copy

def remove_smallest(numbers):
    if not numbers:
        return numbers
    ret = copy.deepcopy(numbers)
    ret.remove(min(ret))
    return ret