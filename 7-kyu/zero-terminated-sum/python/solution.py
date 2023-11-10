import re

def largest_sum(s):
    ptrn = r'0+'
    matches = re.split(ptrn, s)
    if matches is None:
        return 0
    groups = [sum(int(num) for num in group) for group in matches]
    return max(groups)
