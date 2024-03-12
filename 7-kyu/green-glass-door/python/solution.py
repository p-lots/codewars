import re

def step_through_with(s):
    result = re.search(r'(.)\1', s)
    return result is not None
