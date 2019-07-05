def delete_nth(order, max_e):
    counts = {}
    ret = []
    for n in order:
        if n not in counts:
            counts[n] = 1
            ret.append(n)
        else:
            if counts[n] < max_e:
                ret.append(n)
                counts[n] += 1
    return ret