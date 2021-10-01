def construct_submatrix(matrix, rows_to_delete, cols_to_delete):
    ret = []
    rows_i = 0
    rows_to_delete = sorted(rows_to_delete)
    cols_to_delete = sorted(cols_to_delete)
    for i in range(len(matrix)):
        cols_i = 0
        row = []
        if rows_i < len(rows_to_delete) and i == rows_to_delete[rows_i]:
            rows_i += 1
            continue
        for j in range(len(matrix[0])):
            if cols_i < len(cols_to_delete) and j == cols_to_delete[cols_i]:
                cols_i += 1
                continue
            row.append(matrix[i][j])
        if row:
            ret.append(row)
    return ret
