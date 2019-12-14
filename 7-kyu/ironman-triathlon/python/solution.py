def i_tri(s):
    if not s:
        return 'Starting Line... Good Luck!'
    elif s >= 140.6:
        return 'You\'re done! Stop running!'
    key = 'Swim' if s <= 2.4 else 'Bike' if s <= 114.4 else 'Run'
    val = 'Nearly there!' if s >= 130.6 else '{0:.2f} to go!'.format(140.6 - s)
    return {key: val}