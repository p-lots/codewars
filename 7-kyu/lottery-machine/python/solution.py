def lottery(s):
    filter_str = [ch for ch in s if ch.isdigit()]
    if not filter_str:
        return 'One more run!'
    ret = []
    for num in filter_str:
        if num not in ret:
            ret.append(num)
    return ''.join(ret)
