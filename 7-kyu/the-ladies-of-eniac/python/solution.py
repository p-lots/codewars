def rad_ladies(name):
    d = {'%': '', '$': '', '&': '', '/': '', '£': '', '?': '', '@': ''}
    t = str.maketrans(d)
    name = name.translate(t)
    return ''.join(ch for ch in name if not ch.isdigit()).upper()