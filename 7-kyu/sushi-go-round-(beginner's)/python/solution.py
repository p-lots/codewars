def total_bill(s):
    reds = s.count('r')
    return reds * 2 if reds < 5 else reds * 2 - (reds // 5 * 2)
