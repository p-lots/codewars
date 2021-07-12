def uncensor(infected, discovered):
    if not discovered:
        return infected
    disc_iter = iter(discovered)
    return ''.join(next(disc_iter) if ch == '*' else ch for ch in infected)
