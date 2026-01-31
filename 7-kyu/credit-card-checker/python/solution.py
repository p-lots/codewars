def valid_card(card):
    digits = [int(d) for d in card.replace(' ', '')]
    doubled = [(digit * 2 - 9 if digit * 2 > 9 else digit * 2) if idx % 2 == 1 else digit for idx, digit in enumerate(reversed(digits))]
    return sum(doubled) % 10 == 0
