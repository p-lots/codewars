def pyramid(balls):
    ret = 0
    next_row = 1
    while balls > 0:
        ret += 1
        next_row += 1
        balls -= next_row
    return ret
