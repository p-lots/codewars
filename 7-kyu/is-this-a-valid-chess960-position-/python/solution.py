def is_valid(positions):
    first_bishop_idx = positions.index('B')
    second_bishop_idx = positions.rindex('B')
    first_rook_idx = positions.index('R')
    second_rook_idx = positions.rindex('R')
    king_idx = positions.index('K')
    bishops_correct = (first_bishop_idx + second_bishop_idx) % 2 == 1
    king_and_rooks_correct = first_rook_idx < king_idx < second_rook_idx
    return bishops_correct and king_and_rooks_correct
