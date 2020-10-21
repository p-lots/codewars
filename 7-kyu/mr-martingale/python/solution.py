def martingale(bank, outcomes):
    stake = 100
    for outcome in outcomes:
        if outcome == 1:
            bank += stake
            stake = 100
        else:
            bank -= stake
            stake *= 2
    return bank