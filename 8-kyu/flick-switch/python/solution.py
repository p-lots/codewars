def flick_switch(lst):
    flick_lst = []
    flicked = True
    for item in lst:
        if item == 'flick':
            flicked = not flicked
        flick_lst.append(flicked)
    return flick_lst
