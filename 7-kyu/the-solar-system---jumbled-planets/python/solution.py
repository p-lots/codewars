from itertools import pairwise

ORDERING = 'Asteroid < Pluto < Mercury < Mars < Venus < Earth < Neptune < Uranus < Saturn < Jupiter'.split(' < ')

def compare_planets(lhs, rhs):
    lhs_idx = ORDERING.index(lhs)
    rhs_idx = ORDERING.index(rhs)
    if lhs_idx < rhs_idx:
        return '>'
    elif lhs_idx > rhs_idx:
        return '<'
    return '='

def jumbled_solar_system(solar_system):
    return [compare_planets(lhs, rhs) for lhs, rhs in pairwise(solar_system)]
