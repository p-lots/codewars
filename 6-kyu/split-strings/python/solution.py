def solution(s):
    if not s:
        return []
    if len(s) % 2 == 1:
        s += '_'
    i = 0
    ret = []
    for first, second in zip(s, s[1:]):
        if i % 2 == 0:
            ret.append(f'{first}{second}')
        i += 1
    return ret