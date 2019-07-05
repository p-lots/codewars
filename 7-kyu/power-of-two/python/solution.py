def power_of_two(x):
    if x == 1:
        return True
    elif x % 2 == 1:
        return False
    pow = 1
    while pow <= x:
        pow <<= 1
        if pow == x:
            return True
    return False