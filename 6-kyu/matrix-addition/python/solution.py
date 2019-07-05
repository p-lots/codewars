def matrix_addition(a, b):
    ret = []
    for x in range(0, len(a)):
        row = []
        for y in range(0, len(a[0])):
            row.append(a[x][y] + b[x][y])
        ret.append(row)
    return ret