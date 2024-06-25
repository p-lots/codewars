from itertools import zip_longest

def is_defended(attackers, defenders):
    if not attackers and not defenders:
        return True
    elif not defenders:
        return False
    elif not attackers:
        return True
    ret = 0
    for attacker, defender in zip_longest(attackers, defenders, fillvalue=-1):
        if attacker > defender:
            ret -= 1
        elif attacker < defender:
            ret += 1
    if ret == 0:
        if sum(attackers) == sum(defenders):
            return True
        return sum(attackers) < sum(defenders)
    return ret > 0
