def sexy_name(name):
    score = sum(SCORES.get(ch, 0) for ch in name.upper())
    if score >= 600:
        return 'THE ULTIMATE SEXIEST'
    elif 301 <= score <= 599:
        return 'VERY SEXY'
    elif 61 <= score <= 300:
        return 'PRETTY SEXY'
    return 'NOT TOO SEXY'
