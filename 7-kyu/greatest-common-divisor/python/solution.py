def mygcd(x,y):
    while True:
        if x == 0:
            return y
        y %= x
        if y == 0:
            return x
        x %= y