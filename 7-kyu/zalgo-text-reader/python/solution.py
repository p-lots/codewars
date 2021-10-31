def read_zalgo(zalgotext):
    return ''.join(filter(lambda elem: ord(elem) < 127, zalgotext))