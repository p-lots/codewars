import re
def replace_dots(strng):
    return re.sub(r"\.", "-", strng)