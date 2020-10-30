def solve(eq):
    ret = []
    term = ''
    op = ''
    for ch in eq:
        if ch.isalnum():
            term += ch
        elif ch in '*+-/':
            op = ch
            ret.append(term)
            ret.append(op)
            term = ''
            op = ''
    ret.append(term)
    return ''.join(ret[::-1])