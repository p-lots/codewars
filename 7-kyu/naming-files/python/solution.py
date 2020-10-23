def name_file(fmt, nbr, start):
    if nbr <= 0 or not isinstance(nbr, int) or not isinstance(start, int):
        return []
    if fmt.find('<index_no>') == -1:
        return [fmt] * nbr
    ret = []
    for i in range(start, start + nbr, 1):
        fmt_copy = ''.join(ch for ch in fmt)
        fmt_copy = fmt_copy.replace('<index_no>', str(i))
        ret.append(fmt_copy)
    return ret