def hello_world():
    arr = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
    ret = str()
    for n in arr:
        ret += chr(n)
    return ret