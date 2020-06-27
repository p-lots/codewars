def solve(n):
    if n % 10 != 0:
        return -1
    notes = [500, 200, 100, 50, 20, 10]
    ret = 0
    for note in notes:
        while n >= note:
            n -= note
            ret += 1
    return ret