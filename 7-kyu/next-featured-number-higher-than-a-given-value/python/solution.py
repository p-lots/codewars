def is_valid_num(val):
    return val % 2 == 1 and len(set(str(val))) == len(str(val)) and val % 3 == 0

def next_numb(val):
    if val == 9999999999:
        return 'There is no possible number that fulfills those requirements'
    next_val = val + 1
    while not is_valid_num(next_val):
        next_val += 1
    return next_val