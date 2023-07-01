def find_nb(m):
    ret = 0
    while True:
        ret += 1
        m -= ret ** 3
        if m == 0:
            return ret
        elif m < 0:
            return -1
