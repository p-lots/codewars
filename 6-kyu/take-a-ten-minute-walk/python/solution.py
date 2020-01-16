def isValidWalk(walk):
    xdiff, ydiff = 0, 0
    for step in walk:
        if step == 'n':
            ydiff += 1
        elif step == 's':
            ydiff -= 1
        elif step == 'e':
            xdiff += 1
        elif step == 'w':
            xdiff -= 1
    return xdiff == 0 and ydiff == 0 and len(walk) == 10