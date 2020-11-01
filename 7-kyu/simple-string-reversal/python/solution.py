def solve(s):
    s_rev = list(''.join(s[::-1].split()))
    for i, ch in enumerate(s):
        if ch.isspace():
            s_rev.insert(i, ' ')
    return ''.join(s_rev)