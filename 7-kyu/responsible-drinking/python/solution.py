def hydrate(drink_string):
    if not drink_string:
        return None
    split_str = ' and ' if ' and ' in drink_string else ', '
    ret = sum(int(drink.split(' ')[0]) for drink in drink_string.split(split_str))
    plural = 'es' if ret > 1 else ''
    return f'{ret} glass{plural} of water'