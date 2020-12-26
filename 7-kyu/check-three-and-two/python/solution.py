def check_three_and_two(array):
    array_set = list(set(array))
    return len(array_set) == 2 and ((array.count(array_set[0]) == 2 and array.count(array_set[1]) == 3) or \
        (array.count(array_set[1]) == 2 and array.count(array_set[0]) == 3))
