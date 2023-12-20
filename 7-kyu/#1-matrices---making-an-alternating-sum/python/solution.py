def score_matrix(matrix):
    return sum(((-1) ** (row_idx + idx)) * num for row_idx, row in enumerate(matrix) for idx, num in enumerate(row))
