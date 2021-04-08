def any_arrows(arrows):
    return any('damaged' not in arrow.keys() or arrow['damaged'] == False for arrow in arrows)
