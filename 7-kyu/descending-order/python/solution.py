from functools import reduce

def Descending_Order(num):
    return reduce(lambda acc, n: acc * 10 + n, sorted(map(int, str(num)), reverse=True))