def band_name_generator(name):
    return f'{name.title()}{name[1:]}' if name[0] == name[-1] else f'The {name.title()}'
