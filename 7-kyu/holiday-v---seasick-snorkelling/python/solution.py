def sea_sick(sea):
    throw_up_threshhold = 0.2
    ret = sum(first != second for first, second in zip(sea, sea[1:])) / len(sea)
    return 'Throw Up' if ret > throw_up_threshhold else 'No Problem'