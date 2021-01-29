def initialize_names(name):
    name = name.split()
    if len(name) == 1:
        return name[0]
    elif len(name) == 2:
        return ' '.join(name)
    return f'{name[0]} {". ".join(n[0] for n in name[1:-1])}. {name[-1]}'
