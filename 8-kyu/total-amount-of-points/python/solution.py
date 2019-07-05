def points(games):
    ret = 0
    for result in games:
        scores = result.split(':')
        if int(scores[0]) > int(scores[1]):
            ret += 3
        elif int(scores[0]) == int(scores[1]):
            ret += 1
    return ret