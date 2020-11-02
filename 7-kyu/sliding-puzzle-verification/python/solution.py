def is_solved(board):
    curr = 0
    for row in board:
        for elem in row:
            if elem != curr:
                return False
            curr += 1
    return True