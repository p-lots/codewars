# return the minimum required waterbombs to extinguish the fires in the array

from math import ceil

def waterbombs(fire, w):
    if w == 1:
        return fire.count('x')
    return sum(ceil(len(section) / w) for section in fire.split('Y'))