def solution(mtrx):
    for row in mtrx:
        if '>' in row and 'x' in row:
            return row.index('>') < row.index('x')
    return False
