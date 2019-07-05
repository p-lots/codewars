def outed(meet, boss):
    total = 0
    for k, v in meet.items():
        if k == boss:
            total += 2 * v
        else:
            total += v
    result = total / len(meet.items())
    return 'Get Out Now!' if result <= 5 else 'Nice Work Champ!'