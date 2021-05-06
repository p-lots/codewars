def greek_comparator(lhs, rhs):
    lhs_idx = greek_alphabet.index(lhs)
    rhs_idx = greek_alphabet.index(rhs)
    return 0 if lhs_idx == rhs_idx else -1 if lhs_idx < rhs_idx else 1
