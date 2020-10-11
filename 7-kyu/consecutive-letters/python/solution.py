def solve(st):
    st = sorted(st)
    return len(set(st)) == len(st) and all(ord(letter2) == ord(letter1) + 1 for letter1, letter2 in zip(st, st[1:]))