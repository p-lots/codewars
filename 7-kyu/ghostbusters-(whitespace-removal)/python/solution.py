def ghostbusters(building):
    ret = ''.join(ch for ch in building if not ch.isspace())
    return ret if ret != building else "You just wanted my autograph didn't you?"
