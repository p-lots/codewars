def team_comp(heroes):
    if len(heroes) != 6 or len(set(heroes)) != 6:
        raise InvalidTeam()
    ret = [0, 0, 0]
    for hero in heroes:
        if hero in TANK:
            ret[0] += 1
        elif hero in DAMAGE:
            ret[1] += 1
        elif hero in SUPPORT:
            ret[2] += 1
    return ret