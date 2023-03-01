import re

def sum_of_integers_in_string(s):
    return sum(map(int, [elem for elem in re.split(r'\D', s) if elem]))
