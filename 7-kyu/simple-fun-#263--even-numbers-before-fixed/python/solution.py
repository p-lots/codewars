def even_numbers_before_fixed(sequence, fixed_element):
    ret = 0
    for n in sequence:
        if n == fixed_element:
            return ret
        elif n % 2 == 0:
            ret += 1
    return -1