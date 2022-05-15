def coin_combo(cents):
    amts = [25, 10, 5, 1]
    i = 0
    ret = [0, 0, 0, 0]
    while cents > 0:
        while cents >= amts[i]:
            cents -= amts[i]
            ret[i] += 1
        i += 1
    return ret[::-1]
