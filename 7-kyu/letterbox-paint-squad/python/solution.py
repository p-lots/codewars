def paint_letterboxes(start, finish):
    ret = [0] * 10
    for number in range(start, finish + 1):
        for digit in str(number):
            ret[int(digit)] += 1
    return ret
