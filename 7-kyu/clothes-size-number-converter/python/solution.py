import re

def size_to_number(size):
    if size == 'm':
        return 38
    if not (re.match(r'^x*[sl]$', size) or re.match(r'^m$', size)):
        return None
    x_count = size.count('x')
    bases = {'s': 36, 'l': 40}
    return bases['s'] - x_count * 2 if 's' in size else bases['l'] + x_count * 2
