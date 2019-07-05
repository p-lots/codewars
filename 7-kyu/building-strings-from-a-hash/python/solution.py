def solution(pairs):
    if not pairs:
        return ''
    return ','.join('{0} = {1}'.format(key, val) for (key, val) in sorted(pairs.items()))