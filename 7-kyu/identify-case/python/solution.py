import re

def case_id(c_str):
    if re.match(r'^(?:[a-z]+-[a-z]+)+$', c_str) != None:
        return 'kebab'
    elif re.match (r'^(?:[a-z]+_[a-z]+)+$', c_str) != None:
        return 'snake'
    elif re.match(r'^[a-zA-Z]+$', c_str) != None:
        return 'camel'
    return 'none'