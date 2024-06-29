def bin_rota(arr):
    ret = []
    for i, row in enumerate(arr):
        if i % 2 == 1:
            ret.append(row[::-1])
        else:
            ret.append(row)
    return [elem for row in ret for elem in row]
