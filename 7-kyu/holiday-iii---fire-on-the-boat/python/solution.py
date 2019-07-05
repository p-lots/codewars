def fire_fight(s):
    ret = []
    for item in s.split(' '):
        ret.append('~~' if item == 'Fire' else item)
    return ' '.join(ret)