from math import floor

def duck_shoot(ammo, aim, ducks):
    ducks_to_shoot = floor(ammo * aim)
    ret = [ch for ch in ducks]
    for i, target in enumerate(ducks):
        if target == '2' and ducks_to_shoot > 0:
            ret[i] = 'X'
            ducks_to_shoot -= 1
    return ''.join(ret)
