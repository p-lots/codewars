def brightest(colors):
    brightest = lambda c: max([int(c[1:3], 16), int(c[3:5], 16), int(c[5:], 16)])
    return max(colors, key=brightest)
