def ranking(people):
    if not people:
        return []
    ret = sorted(people, key=lambda item: (-item['points'], item['name']))
    actual_pos = 1
    tracked_pos = 1
    prev = ret[0]['points']
    ret[0]['position'] = 1
    for i in range(1, len(ret)):
        actual_pos += 1
        if ret[i]['points'] != prev:
            tracked_pos = actual_pos
        ret[i]['position'] = tracked_pos
        prev = ret[i]['points']
    return ret
    