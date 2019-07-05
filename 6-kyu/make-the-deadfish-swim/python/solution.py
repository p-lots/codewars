def parse(data):
    val = 0
    ret = []
    for item in data:
        if item == 'i':
            val += 1
        elif item == 'd':
            val -= 1
        elif item == 's':
            val **= 2
        elif item == 'o':
            ret.append(val)
    return ret