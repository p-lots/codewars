import re

def array_info(x):
    if not x:
        return 'Nothing in the array!'
    arr_length = len(x)
    num_ints = sum(isinstance(n, int) for n in x) or None
    num_floats = sum(isinstance(n, float) for n in x) or None
    num_strs = sum(isinstance(n, str) and (re.match(r'\s+', n) == None) for n in x) or None
    num_whitespace = sum(isinstance(n, str) and (re.match(r'\s+', n) != None) for n in x) or None
    return [[arr_length], [num_ints], [num_floats], [num_strs], [num_whitespace]]
