def ones_counter(inp):
    ret = []
    curr_count = 0
    for n in inp:
        if n == 1:
            curr_count += 1
        elif n == 0 and curr_count > 0:
            ret.append(curr_count)
            curr_count = 0
    if curr_count > 0:
        ret.append(curr_count)
    return ret
