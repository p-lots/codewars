def find_unknown_number(x, y, z):
    ret = 1
    while True:
        if ret % 3 == x and ret % 5 == y and ret % 7 == z:
            break
        ret += 1
    return ret