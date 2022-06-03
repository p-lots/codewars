def is_flush(cards):
    return all(lhs[-1] == rhs[-1] for lhs, rhs in zip(cards, cards[1:]))
