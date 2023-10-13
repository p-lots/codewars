def speed_limit(speed, signals):
    total_fine = 0
    for signal in signals:
        overage = speed - signal
        if 10 <= overage <= 19:
            total_fine += 100
        elif 20 <= overage <= 29:
            total_fine += 250
        elif overage >= 30:
            total_fine += 500
    return total_fine