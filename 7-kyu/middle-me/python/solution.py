def middle_me(N, X, Y):
    return f'{Y * (N // 2)}{X}{Y * (N // 2)}' if N % 2 == 0 else X
