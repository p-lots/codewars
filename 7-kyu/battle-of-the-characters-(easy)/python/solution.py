from string import ascii_uppercase

def battle(x, y):
    LOOKUP = {k: v for k, v in zip(ascii_uppercase, range(1, 27))}
    score = lambda s: sum(LOOKUP[ch] for ch in s)
    x_score = score(x)
    y_score = score(y)
    return x if x_score > y_score else 'Tie!' if x_score == y_score else y
