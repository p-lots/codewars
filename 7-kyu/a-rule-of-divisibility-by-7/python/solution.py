from math import log10

def seven(m):
    steps = 0
    if m < 1:
        return (m, steps)
    while log10(m) > 2:
        m = (m // 10) - ((m % 10) * 2)
        steps += 1
        if m < 1:
            break
    return (m, steps)